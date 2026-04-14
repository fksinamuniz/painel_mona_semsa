import re

# Read the current metas.ts file
with open(r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\src\lib\metas.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Actions extracted from PAS 2026 text, mapped by meta number
ACTIONS = {
    "1.1.1": [
        "Mapear áreas descobertas e planejar a implantação das novas equipes de Saúde da Família",
        "Dimensionar o pessoal necessário para compor as equipes e solicitar o provimento quando necessário",
        "Revisar o cadastro territorial das equipes de Saúde da Família (eSF), ajustando a área de abrangência das equipes para garantir que o número de pessoas por equipe não exceda o limite preconizado"
    ],
    "1.1.2": [
        "Elaborar um plano de recursos humanos que preveja a reposição de vagas de ACS abertas por aposentadoria, exoneração ou licenças de longa duração, minimizando a perda de cobertura",
        "Dimensionar o pessoal necessário para compor as novas eSF e solicitar o provimento quando necessário"
    ],
    "1.1.3": [
        "Solicitar junto ao Ministério da Saúde o credenciamento das novas equipes multiprofissionais de acordo com o cronograma de implantação",
        "Mapear as áreas e Equipes de Saúde da Família (eSF) que mais necessitam de apoio matricial, definindo o tipo de eMulti a ser implantada em cada território para otimizar o uso do recurso",
        "Realizar o dimensionamento de pessoal necessário para compor as equipes e solicitar o provimento quando necessário",
        "Adquirir insumos, materiais de consumo e equipamentos de uso das eMultis"
    ],
    "1.1.4": [
        "Elaborar, em parceria com as redes de Atenção à Saúde e a Secretaria Municipal de Assistência Social o Diagnóstico Situacional da população em situação de rua no município, identificando a localização, o perfil de saúde e as necessidades, para justificar tecnicamente a implantação da eCR",
        "Solicitar o novo credenciamento ao Ministério da Saúde da equipe de Consultório na Rua (eCR) na plataforma e-GestorAPS",
        "Realizar o dimensionamento de pessoal necessário para compor as equipes e solicitar o provimento quando necessário",
        "Criar um fluxo de trabalho formal com a Assistência Social (Centro POP), Segurança Pública e ONGs que atuam com a população de rua, garantindo a retaguarda social e a segurança da equipe em campo",
        "Aquirir um veículo adequado e seguro para o transporte da equipe e dos materiais de saúde, adaptado para o trabalho em diferentes pontos da cidade",
        "Prover kits de saúde portáteis (medicamentos básicos, curativos, testes rápidos, aferição de pressão/glicemia) para garantir que a equipe tenha resolutividade básica no local de atendimento"
    ],
    "1.1.5": [
        "Encaminhar processo para aquisição de veículos adaptados e exclusivos para o Transporte Sanitário Eletivo, em conformidade com as normas sanitárias e de acessibilidade vigentes",
        "Garantir, anualmente na Programação Anual de Saúde (PAS), a previsão orçamentária para o custeio da frota, contemplando contratação/capacitação de motoristas, combustível, seguro, manutenção preventiva e corretiva dos veículos",
        "Estabelecer plano de manutenção preventiva e escala de motoristas capacitados em direção defensiva e primeiros socorros para atuar nessas rotas específicas"
    ],
    "1.1.6": [
        "Encaminhar processo para aquisição de frota específica e adaptada (veículos 4x4) de uso exclusivo das equipes da Atenção Primária à Saúde vinculadas às áreas rurais e de difícil acesso",
        "Garantir, anualmente na Programação Anual de Saúde (PAS), a previsão orçamentária para o custeio da frota, contemplando contratação/capacitação de motoristas, combustível, seguro, manutenção preventiva e corretiva dos veículos",
        "Estabelecer plano de manutenção preventiva e escala de motoristas capacitados em direção defensiva e primeiros socorros para atuar nessas rotas específicas"
    ],
    "1.1.7": [
        "Definir a \"Cesta de Itens Prioritários\" por tipo de unidade, garantindo que itens críticos nunca fiquem abaixo do estoque de segurança",
        "Estruturar e otimizar as rotas logísticas de distribuição entre a Central de Abastecimento Farmacêutico e o Almoxarifado e as Unidades Básicas de Saúde, garantindo que as cotas mensais de materiais cheguem nos prazos corretos",
        "Encaminhar processo para aquisição de itens de custeio para a Atenção Primária à Saúde",
        "Encaminhar processo para contratação de serviços de manutenção (refrigeração, impressão, equipamentos odontológicos e hospitalares) para as Unidades Básicas de Saúde"
    ],
    "1.1.8": [
        "Realizar inventário físico, tecnológico e patrimonial em todas as UBS, atualizando as informações de equipamentos instalados diretamente no Sistema de Cadastro Nacional de Estabelecimentos de Saúde (CNES)",
        "Encaminhar processo para aquisição de materiais permanentes, equipamentos médico-hospitalares, odontológicos, imobiliários e de tecnologia da informação (TI)",
        "Encaminhar processo para executar reformas, ampliações e adequações elétricas/hidráulicas nas unidades existentes para que comportem as novas tecnologias adquiridas, garantindo a acessibilidade"
    ],
    "1.1.9": [
        "Elaborar projeto de reforma das Unidades Básicas de Saúde de acordo com o cronograma da APS",
        "Contratar empresa especializada para a reforma das UBS, de acordo com cronograma da APS",
        "Adquirir equipamentos e materiais permanentes para as UBS"
    ],
    "1.1.10": [
        "Elaborar projeto de ampliação das Unidades Básicas de Saúde de acordo com o cronograma da APS",
        "Contratar empresa especializada para a ampliação das UBS, de acordo com cronograma da APS",
        "Adquirir equipamentos e materiais permanentes para as UBS"
    ],
    "1.1.11": [
        "Acompanhar a execução da obra da UBS VS10",
        "Adquirir equipamentos e materiais permanentes para as UBS VS10 que está em fase de construção",
        "Contratar empresa especializada para a construção de uma Unidade Básica de Saúde no bairro Nova Carajás",
        "Identificar áreas institucionais existentes nos territórios para ampliação da cobertura da APS",
        "Captar recursos via Governo Federal (Programas ou Emenda Parlamentar). Após a aprovação da proposta e a garantia do recurso (seja por programa ou emenda), cumprir todas as exigências documentais do Ministério da Saúde (ex: documentação do terreno, certidões negativas). Assinar o Termo de Convênio/Compromisso",
        "Elaborar projeto básico e executivo das UBS seguindo as normas da ANVISA (RDC 50) e os padrões do Ministério da Saúde para tipologia de UBS (Porte I, II ou III)"
    ],
    "1.1.12": [
        "Reorganizar o processo de trabalho nas UBS para garantir acesso oportuno para demandas agudas e crônicas, minimizando a necessidade de busca por serviços de urgência e emergência hospitalar",
        "Manter o serviço de acolhimento à demanda espontânea diariamente em todas as Unidades Básicas de Saúde",
        "Identificar e realizar busca ativa de pacientes com condições crônicas de alto risco (diabetes e hipertensão descompensados), garantindo a captação e o acompanhamento regular",
        "Realizar reuniões de análise de dados com as equipes, identificando as principais causas de ICSAP por território (UBS/eSF) para direcionar as ações de intervenção mais urgentes"
    ],
    "1.1.13": [
        "Incluir a oferta de PICS (principalmente em grupo) no rol de serviços das equipes de Saúde da Família e das equipes multiprofissionais",
        "Identificar e capacitar profissionais internos da rede (que já tenham experiência ou formação em PICS) para atuarem como facilitadores/instrutores no próprio município, promovendo a autonomia da gestão na Educação Permanente",
        "Assegurar o registro correto de todas as sessões de PICS realizadas no SISAB, utilizando os códigos de procedimento específicos (Ficha de Atividade Coletiva ou Ficha de Atendimento Individual)",
        "Adquirir materiais de consumo e equipamentos para a realização das PICS"
    ],
    "1.1.14": [
        "Incluir a avaliação nutricional em todas consultas de rotina (pré-natal, puericultura, hipertensos, diabéticos) e atendimentos multidisciplinares",
        "Integrar a avaliação nutricional a campanhas de vacinação e ações de prevenção em massa nas UBS e nos territórios (escolas, centros comunitários, comunidades rurais)",
        "Prover novos equipamentos antropométricos e insumos de medição, acompanhando o cronograma de compras e manutenção preventiva para assegurar a continuidade do registro do estado nutricional nas UBS"
    ],
    "1.1.15": [
        "Realizar uma ação assistencial com consultas e procedimentos de enfermagem, nutrição e dispensação de medicamentos a cada semestre",
        "Realizar ações de acompanhamento das condicionalidades do Programa Bolsa Família (Pré-natal, situação vacinal, avaliação nutricional)",
        "Realizar atendimentos odontológicos com atividades coletivas de escovação dental supervisionada"
    ],
    "1.1.16": [
        "Mapear as populações rurais do município de Parauapebas e da área do contestado, baseado no Termo de Cooperação 001/2025, identificando as demandas de saúde das populações rurais, respeitando a sua organização social, cultura, religião e o território",
        "Estabelecer cronogramas de ações estratégicas que visem melhorar as condições de vida e saúde nas comunidades rurais que não possuem cobertura de equipes de Atenção Primária à Saúde",
        "Identificar e solicitar os recursos (pessoal e insumos) necessários para levar assistência em saúde a essas comunidades",
        "Condensar os dados epidemiológicos de forma que forneçam informações estruturais para subsidiar as tomadas de decisão de forma qualificada"
    ],
    "1.1.17": [
        "Ampliar o rastreamento e o diagnóstico precoce de hipertensão arterial, diabetes mellitus, dislipidemias e cânceres mais prevalentes (mama, colo de útero, próstata e colorretal)",
        "Capacitar equipes da APS em abordagem integral das DCNT, estratificação de risco e educação em saúde",
        "Desenvolver ações intersetoriais voltadas para alimentação saudável, atividade física, combate ao tabagismo, consumo nocivo de álcool e redução do estresse",
        "Realizar Campanhas educativas anuais (\"Dia Mundial do Coração\", \"Novembro Azul\", \"Outubro Rosa\")",
        "Ampliar acesso a consultas especializadas e exames de média complexidade (cardiologia, endocrinologia, oncologia, pneumologia)"
    ],
    "1.1.18": [
        "Capacitar as equipes de saúde sobre os procedimentos corretos de registro, a importância do acompanhamento e o preenchimento das condicionalidades de saúde",
        "Pactuar com a Secretaria Municipal de Educação a solicitação do número do NIS no ato da matrícula dos alunos da rede pública de ensino, para o acompanhamento dos alunos beneficiários durante as ações do PSE",
        "Implementar rotinas trimestrais de busca ativa focada nas famílias não acompanhadas",
        "Realizar campanhas de comunicação contínuas nas UBS e canais digitais sobre a importância do acompanhamento de saúde para a permanência no PBF",
        "Realizar mutirões em datas estratégicas para facilitar o acesso de famílias com dificuldade de comparecimento, principalmente aquelas que residem em áreas descobertas por equipes de Saúde da Família"
    ],
    "1.1.19": [
        "Promover treinamento prático intensivo para os profissionais de saúde que realizam puericultura, abordando a aplicação, pontuação e interpretação do M-CHAT-R, bem como a comunicação sensível do resultado com as famílias",
        "Incluir o M-CHAT-R na rotina de atendimento das consultas de puericultura na idade de 16 e 30 meses"
    ],
    "1.1.20": [
        "Encaminhar processo para compra de equipamentos de Tecnologias de Informação e Comunicação (TIC) adequados (computadores com câmera de alta resolução, headsets, monitores duplos) para estruturar as salas de telessaúde nas UBS",
        "Desenvolver atividades de formação para as equipes de Saúde da Família (médicos, enfermeiros, agentes comunitários) sobre letramento digital, uso das plataformas (como o e-SUS APS) e protocolos operacionais para a realização de teleinterconsultas e telediagnósticos",
        "Estabelecer o fluxo técnico integrando os pontos de telessaúde da APS ao Complexo Regulador Municipal (SISREG/e-SUS Regulação). A teleconsultoria entre o médico da família (na UBS) e o especialista deve servir como ferramenta para qualificar o encaminhamento ou resolver o caso localmente, evitando deslocamentos desnecessários e reduzindo a fila de espera física"
    ],
    "1.1.21": [
        "Intensificar a importância do acompanhamento adequado da gestante e identificação precoce de riscos que possam comprometer o nascimento e a sobrevivência do bebê",
        "Promover parto seguro e humanizado, reduzindo complicações neonatais e maternas",
        "Fortalecer a prevenção de infecções e agravos preveníveis por vacina e a melhora do estado nutricional infantil",
        "Fortalecer a atenção ao recém-nascido e à puericultura",
        "Reforçar a vigilância e investigação dos óbitos infantis e fetais"
    ],
    "1.1.22": [
        "Instituir o uso obrigatório e sistemático da Caderneta da Criança em todas as consultas, com foco no preenchimento dos marcos do desenvolvimento neuropsicomotor",
        "Organizar a agenda das Equipes de Saúde da Família (ESF) para garantir as consultas de rotina (crescimento e desenvolvimento) da primeira infância, promovendo a busca ativa de crianças faltosas nas consultas e no calendário vacinal",
        "Encaminhar processo para aquisição e manutenção dos equipamentos antropométricos adequados nas UBS (balanças pediátricas digitais, réguas antropométricas) e assegurar a disponibilidade de insumos básicos",
        "Estabelecer um fluxo regulatório rápido entre a Atenção Primária e a Atenção Especializada para os casos em que a ESF identifique atrasos no desenvolvimento neuropsicomotor da criança (ex: encaminhamento para estimulação precoce no CER IV ou no ambulatório de alto risco)"
    ],
    "1.1.23": [
        "Ampliar o acesso ao financiamento e a qualidade do pré-natal, com enfoque na detecção precoce de agravos",
        "Fortalecer a vigilância epidemiológica e a investigação dos óbitos maternos",
        "Assegurar a ligação eficiente entre a atenção básica e o local de parto",
        "Fortalecer o suporte de equipes multiprofissionais à mulher, o que inclui apoio psicológico e orientação sobre amamentação e cuidados com o bebê",
        "Fortalecer o acesso a métodos contraceptivos e informações sobre saúde sexual e reprodutiva, permitindo que as mulheres planejem suas gestações",
        "Fortalecer a Rede Alyne"
    ],
    "1.1.24": [
        "Prover o acesso à primeira consulta de pré-natal até a 12ª semana de gestação",
        "Identificar as gestantes que faltaram à consulta agendada e realizar a busca ativa para reagendamento do acompanhamento",
        "Assegurar o fornecimento ininterrupto de insumos básicos (sulfato ferroso, ácido fólico)",
        "Pactuar fluxo ágil dos exames laboratoriais de rotina (Tipagem Sanguínea, Glicemia, VDRL, Testes Rápidos)"
    ],
    "1.1.25": [
        "Realizar grupos de saúde de adolescentes nas UBSs com temas diversos, incluindo prevenção de IST/AIDS, planejamento familiar, autocuidado e tomada de decisão responsável",
        "Fortalecer parcerias institucionais no combate à violência sexual contra crianças e adolescentes",
        "Monitorar a implementação do protocolo de escuta especializada de crianças e adolescentes vítimas ou testemunhas de violências nos serviços de saúde"
    ],
    "1.1.26": [
        "Utilizar o sistema de informação da APS para gerar uma lista nominal de mulheres de 25 a 64 anos que não realizaram o exame nos últimos 36 meses e realizar a busca ativa",
        "Realizar ações de saúde itinerantes ou educativas em locais com grande concentração de mulheres, oferecendo agendamento facilitado e material educativo",
        "Organizar, pelo menos uma vez por mês, horários de atendimento estendidos nas UBS para a coleta de Papanicolau e outros exames ginecológicos, visando atender a população que trabalha em horário comercial",
        "Analisar o percentual de rastreamento separadamente por subgrupos (25-34 anos; 35-49 anos; 50-64 anos) para identificar onde a cobertura está mais crítica e direcionar campanhas específicas"
    ],
    "1.1.27": [
        "Implementar rotinas de busca ativa por meio dos Agentes Comunitários de Saúde (ACS) e equipes da Atenção Primária para identificar mulheres e homens transgêneros na faixa de 50 a 69 anos, garantindo o agendamento do exame e a \"navegação\" (acompanhamento) do usuário pela Rede de Atenção à Saúde para evitar o absenteísmo",
        "Utilizar os dados do PEC para identificar todas as mulheres na faixa de 50 a 74 anos por território, sinalizando aquelas com exames vencidos há mais de dois anos",
        "Pactuar e organizar o fluxo na Central de Regulação Municipal para que casos suspeitos (BI-RADS 4 ou 5) identificados no rastreamento tenham acesso prioritário e garantido à consulta com mastologista e à biópsia (punção por agulha grossa/fina) em tempo oportuno (Lei dos 30 dias)"
    ],
    "1.1.28": [
        "Organizar as agendas das Equipes de Saúde da Família (eSF) para garantir o cuidado contínuo e rastreio de pacientes diabéticos faltosos, assegurando o registro adequado dos exames de hemoglobina glicada e avaliação de risco cardiovascular",
        "Classificar os pacientes diabéticos por grau de risco (baixo, médio, alto) no PEC, definindo a periodicidade das consultas e exames para cada perfil",
        "Encaminhar, junto à Assistência Farmacêutica, processo para aquisição e dispensação contínua de medicamentos essenciais e insumos para automonitoramento da glicemia capilar (tiras reagentes, glicosímetros, canetas aplicadoras e insulinas)",
        "Instituir protocolos na APS para a avaliação periódica dos pés diabéticos (prevenção de amputações) e do fundo de olho (prevenção de cegueira), utilizando o apoio matricial das Equipes Multiprofissionais (eMulti)",
        "Desenvolver atividades coletivas focadas no estímulo à alimentação adequada e à prática de atividades físicas para controle metabólico, reduzindo os fatores de risco (sobrepeso e obesidade)"
    ],
    "1.1.29": [
        "Organizar as agendas das Equipes de Saúde da Família (eSF) para garantir o cuidado contínuo, a aferição da pressão arterial e a busca ativa de pacientes hipertensos faltosos, assegurando o registro adequado no Prontuário Eletrônico",
        "Encaminhar processo para contratualização de prestação de serviço de manutenção e aquisição regular de esfigmomanômetros (aparelhos de pressão) e estetoscópios para todas as UBS",
        "Encaminhar, junto à Assistência Farmacêutica, processo para aquisição e dispensação contínua de medicamentos anti-hipertensivos (como Losartana, Captopril, Enalapril, etc.) nas farmácias das UBS",
        "Viabilizar, junto ao Laboratório Municipal, a realização anual de exames básicos de monitoramento (Creatinina, ECG, Perfil Lipídico e Potássio)",
        "Desenvolver atividades coletivas e educação em saúde com o apoio das Equipes Multiprofissionais (eMulti), focando na promoção da atividade física, controle do tabagismo e redução do consumo de sal/sódio"
    ],
    "1.1.30": [
        "Instituir a rotina obrigatória de aplicação da Avaliação Multidimensional da Pessoa Idosa e do Índice de Vulnerabilidade Clínico Funcional (IVCF-20) por parte das Equipes de Saúde da Família (eSF), classificando os idosos em independentes, com risco de fragilização ou frágeis",
        "Integrar na consulta de rotina da APS a aplicação de testes de mobilidade (como o Timed Up and Go) e a avaliação do ambiente domiciliar por meio dos Agentes Comunitários de Saúde (ACS)",
        "Realizar oficinas coletivas com idosos e cuidadores sobre adaptações domiciliares seguras (retirada de tapetes, melhoria da iluminação) e a importância da atividade física para fortalecimento muscular",
        "Viabilizar o acesso prioritário a exames laboratoriais e de imagem para idosos com critérios de fragilidade estabelecidos, integrando os dados com a regulação municipal"
    ],
    "1.1.31": [
        "Promover a prevenção de quedas e promover envelhecimento saudável, junto à APS",
        "Assegurar continuidade e integralidade do cuidado",
        "Implementar a Linha de Cuidado da Pessoa Idosa com foco em prevenção de quedas"
    ],
    "1.1.32": [
        "Mapear áreas descobertas e planejar a implantação das novas equipes de Saúde Bucal",
        "Dimensionar o pessoal necessário para compor as equipes e solicitar o provimento quando necessário",
        "Vincular novas eSB às Equipes de Saúde da Família (eSF) em operação, assegurando o trabalho em conjunto no território e a adscrição de usuários",
        "Elaborar um Plano de Investimento em Odontologia para a aquisição de novos equipamentos odontológicos (cadeiras, compressores, fotopolimerizadores) para as novas equipes",
        "Prover a manutenção preventiva e corretiva dos consultórios em funcionamento",
        "Adquirir insumos, materiais de consumo e instrumentais odontológicos",
        "Manter os atendimentos odontológicos realizados nas Unidades Odontológicas Móveis – UOMs",
        "Realizar convênio com Laboratório Regional de Próteses Dentárias – LRPD"
    ],
    "1.1.36": [
        "Mapear pessoas com deficiência adscritas nas microáreas das equipes de Saúde da Família",
        "Promover educação permanente e continuada das equipes de Saúde da família e equipes de Saúde Bucal de referência quanto ao cadastro das Pessoas com Deficiência no Sistema de Informação Vigente, com ofertas de oficinas de sensibilização sobre acessibilidade e inclusão",
        "Criar fluxos preferenciais de atendimento para PcDs com mobilidade reduzida ou dependentes de transporte"
    ],
    "1.1.37": [
        "Formalizar o convênio/contrato com o Laboratório Regional de Prótese Dentária (LRPD), garantindo a adequação dos cadastros no CNES (Subtipo de Estabelecimento 39.03) e a vinculação do profissional Protético Dentário (CBO 3224-10)",
        "Instituir e padronizar o protocolo clínico de referência e contrarreferência para reabilitação protética nas Unidades Básicas de Saúde (UBS)",
        "Parametrizar os sistemas de faturamento municipal para o registro rigoroso da produção do LRPD",
        "Apresentar a prestação de contas da produção protética ao Conselho Municipal de Saúde"
    ],
    "1.1.38": [
        "Instituir e oficializar um protocolo de fluxo interno nas Unidades Básicas de Saúde (UBS) denominado \"Pré-Natal Odontológico\"",
        "Integrar os Agentes Comunitários de Saúde (ACS) na captação de gestantes faltosas",
        "Realizar atividades educativas durante as reuniões de grupos de gestantes, abordando mitos sobre o tratamento odontológico na gravidez e a importância da higiene bucal para a saúde do binômio mãe-filho"
    ],
    "1.1.39": [
        "Garantir espaço protegido na carga horária semanal das Equipes de Saúde da Família (eSF), Equipes de Atenção Primária (eAP), Equipes de Saúde Bucal (eSB) e equipes Multiprofissionais (eMulti) para atividades de Educação Permanente em Saúde (EPS) dentro da própria UBS",
        "Executar o programa \"Qualifica SUS Parauapebas\" focado exclusivamente no perfil de morbimortalidade local (Diagnóstico Situacional)",
        "Fomentar o uso de plataformas de educação à distância e teleconsultorias formativas",
        "Instituir um sistema de controle de Recursos Humanos (plataforma digital ou planilhas do Setor de Ações Educacionais) para rastrear nominalmente a carga horária de treinamento de cada servidor"
    ],
    "2.1.7": [
        "Realizar capacitação permanente dos servidores vinculados ao componente SAMU 192, com os cursos obrigatórios",
        "Comprovar a vigência do seguro contra sinistro para as Unidades Móveis",
        "Contratar manutenção das Unidades Móveis SAMU 192",
        "Adquirir os uniformes das equipes assistenciais, obedecendo ao padrão visual estabelecido pelo Ministério da Saúde, e Equipamentos de Proteção Individual (EPI)",
        "Reformar a Base Descentralizada mantendo a padronização visual, conforme normatização específica constante do manual de identidade visual do Ministério da Saúde",
        "Adquirir e realizar a manutenção preventiva e corretiva dos equipamentos médicos"
    ],
    "2.1.8": [
        "Aperfeiçoar a articulação com a Central de Regulação das Urgências - CRU para manter o tempo médio total de regulação em até 5 minutos",
        "Integrar ações com o Núcleo Interno de Regulação -NIR do Hospital Geral de Parauapebas - HGP para agilizar a confirmação e liberação de leitos",
        "Monitorar intervalo entre o acionamento e saída da base das equipes operacionais",
        "Manter o funcionamento do sistema de comunicação entre CRU e equipe (celular ativo)",
        "Qualificar 02 serviços existentes (Unidade de Suporte Básico e Unidade de Suporte Avançado)",
        "Participar das ações educativas nos serviços de saúde e na comunidade",
        "Implantar sistemas de informação para apoiar a gestão e o monitoramento das ações",
        "Realizar a manutenção preventiva e corretiva na frota do SAMU",
        "Construir duas bases descentralizadas",
        "Adquirir 02 motolâncias",
        "Ampliar frota de Unidade de Suporte Básico - USB",
        "Implantar e habilitar três novos serviços (uma ambulância USB e duas motolâncias)",
        "Adquirir equipamentos e materiais permanentes necessários ao funcionamento do serviço"
    ],
    "2.1.21": [
        "Submeter 100% dos leitos de retaguarda clínica à regulação integral pelas Centrais de Regulação de Leitos e gerenciar o fluxo interno através do Núcleo Interno de Regulação (NIR)",
        "Implantar rondas e visitas multidisciplinares horizontais diárias nas enfermarias clínicas de retaguarda, utilizando prontuário único",
        "Alimentar rigorosa e mensalmente o Sistema de Informações Hospitalares (SIH/SUS) com a produção e as Autorizações de Internação Hospitalar (AIH) destes leitos"
    ],
    "2.1.24": [
        "Definir territórios prioritários para implantação das novas equipes com base em indicadores epidemiológicos e sociodemográficos",
        "Elaborar plano de dimensionamento de pessoal e ampliação orçamentária para 02 equipes EMAD",
        "Adquirir transporte compatível com a necessidade de deslocamento, conforme Portaria GM/MS Nº 3.005 de 2024",
        "Adquirir equipamentos para acomodação da equipe na sede do SAD (cadeiras, mesas, computadores compatíveis com os sistemas e equipamentos de refrigeração adequada)",
        "Ampliar a cobertura territorial da Atenção Domiciliar para atendimento das áreas rurais de Parauapebas",
        "Realizar capacitações iniciais para integração dos novos profissionais às diretrizes do SAD",
        "Solicitar habilitação e cofinanciamento federal via programa Melhoria da Atenção Domiciliar",
        "Integrar as equipes EMAD com as ESF, CAPS, Atenção Especializada e Rede de Urgência"
    ],
    "2.2.9": [
        "Mapear as demandas das equipes da APS e identificar aquelas que ainda estão sem apoio matricial sistemático para acompanhamento",
        "Construir cronograma com as ações de matriciamento conforme demandas apresentadas pela APS",
        "Adquirir transporte institucional e logística para deslocamento das equipes do CAPS até as unidades da APS",
        "Estabelecer ações coletivas conjuntas, quando indicado, entre APS e CAPS",
        "Monitorar a realização de visitas compartilhadas, quando necessário, entre CAPS e APS",
        "Planejar Educação Permanente para as equipes da APS em temas prioritários (saúde mental, abordagem de sofrimento psíquico, manejo de casos leves e moderados, prevenção do suicídio, acolhimento, uso de substâncias, cuidado compartilhado)"
    ],
    "2.2.10": [
        "Realizar diagnóstico situacional da cobertura de saúde mental no município, utilizando dados do Prontuário Eletrônico vigente",
        "Identificar a população de referência e estimar a demanda potencial por serviços de saúde mental conforme parâmetros do Ministério da Saúde",
        "Fortalecer a articulação entre o CAPS II e a Atenção Primária à Saúde (APS), conforme diretrizes da RAPS",
        "Manter a estratégias de matriciamento em saúde mental junto às equipes da APS",
        "Ampliar o acesso às ações de saúde mental no território, incluindo atendimentos individuais e coletivos",
        "Qualificar os registros em saúde mental no sistema eletrônico vigente, visando melhoria dos indicadores e monitoramento",
        "Monitorar e avaliar periodicamente os indicadores de cobertura em saúde mental, conforme parâmetros do Ministério da Saúde"
    ],
    "2.3.6": [
        "Identificar programas federais de financiamento destinados ao transporte sanitário adaptado",
        "Elaborar proposta técnica para adesão ao incentivo financeiro",
        "Registrar e encaminhar solicitação de adesão ao Ministério da Saúde",
        "Estruturar plano para o transporte sanitário para usuários do CER",
        "Garantir uso prioritário do transporte para pacientes com deficiência e mobilidade reduzida"
    ],
    "2.3.7": [
        "Ampliar a oferta de atendimentos de reabilitação nas áreas física, auditiva, visual e intelectual, de acordo com a demanda identificada",
        "Realizar diagnóstico da demanda reprimida",
        "Reorganizar e otimizar os fluxos de acesso e agendamento de usuários para os serviços de reabilitação, reduzindo o tempo de espera e evitando o absenteísmo",
        "Prover a manutenção de equipamentos, mobiliários e materiais específicos de reabilitação",
        "Implementar protocolos de atendimento e acompanhamento terapêutico, padronizando condutas e otimizando o tempo de reabilitação por usuário",
        "Ampliar o monitoramento dos indicadores em reabilitação, utilizando sistemas de informação (como o SIA/SUS) para acompanhamento contínuo da meta"
    ],
    "2.4.3": [
        "Ampliar a oferta de consultas nas especialidades prioritárias (neurologia, cardiologia, ginecologia, ortopedia, reumatologia e endocrinologia) na Policlínica Municipal",
        "Reorganizar as agendas dos profissionais das especialidades prioritárias, otimizando a utilização dos horários disponíveis para atendimento",
        "Avaliar a necessidade de ampliação da carga horária ou contratação complementar de profissionais especialistas conforme demanda assistencial",
        "Implantar estratégias para redução do absenteísmo nas consultas especializadas, incluindo confirmação prévia de consultas e reorganização das vagas não utilizadas",
        "Ampliar a realização de atendimentos multiprofissionais e atividades de cuidado compartilhado que contribuam para resolutividade das demandas especializadas",
        "Otimizar os fluxos internos de atendimento na Policlínica para melhorar a produtividade assistencial"
    ],
    "2.4.4": [
        "Realizar levantamento das necessidades assistenciais prioritárias do município para definição das modalidades de OCIs a serem implantadas",
        "Definir e formalizar as modalidades de Ofertas de Cuidados Integrados (OCI's) a serem implantadas na rede municipal",
        "Elaborar protocolos assistenciais e fluxos de encaminhamento e contrarreferência para execução das OCIs",
        "Realizar análise e conversão progressiva das filas de consultas e exames em Ofertas de Cuidados Integrados (OCI)",
        "Mapear serviços da rede própria e da rede complementar aptos a executar as OCIs",
        "Formalizar demanda para credenciamento de serviços especializados, quando necessário, para execução das Ofertas de Cuidados Integrados (OCI's), garantindo a ampliação da capacidade assistencial da rede municipal",
        "Capacitar profissionais da rede municipal e serviços credenciados quanto aos fluxos assistenciais e critérios de encaminhamento das OCIs",
        "Implantar as modalidades de OCI nos serviços da rede própria e credenciada",
        "Monitorar a execução das OCIs e avaliar os resultados assistenciais"
    ],
    "2.4.5": [
        "Realizar levantamento da demanda reprimida e do tempo de espera para exames de diagnóstico por imagem no município",
        "Mapear a capacidade instalada da rede própria e da rede contratualizada para realização de exames de imagem",
        "Ampliar a oferta de exames de imagem na rede própria mediante reorganização das agendas e ampliação de turnos de atendimento",
        "Formalizar demanda para credenciamento ou contratação de serviços especializados para realização de exames de diagnóstico por imagem, conforme necessidade assistencial",
        "Reorganizar os fluxos de solicitação, autorização e agendamento de exames de diagnóstico por imagem por meio da regulação municipal, com elaboração e implantação de protocolos clínicos para solicitação e priorização dos exames"
    ],
    "2.4.6": [
        "Elaborar o plano municipal de redução de filas e submetê-lo à pactuação na CIB estadual",
        "Fortalecer a atuação do Núcleo Interno de Regulação (NIR) do HGP"
    ],
    "2.5.3": [
        "Manter a oferta de consultas especializadas para acompanhamento de gestantes de alto risco na Policlínica Municipal, com qualificação do processo de registro e codificação dos procedimentos no SIA/SUS, garantindo a correta identificação das consultas de pré-natal de alto risco"
    ],
    "2.5.4": [
        "Identificar o número de gestantes de risco habitual e alto risco e a demanda mensal de exames",
        "Mapear a capacidade instalada do laboratório central de Parauapebas",
        "Viabilizar a oferta dos exames preconizados pelo Ministério da Saúde para as gestantes",
        "Fazer formalização de solicitação de demanda para serviços de laboratórios privados, insumos e equipamentos para ampliação da oferta, quando necessário",
        "Fortalecer pontos de coleta de exames nas Unidade Básicas de Saúde (UBS)",
        "Proporcionar agendamento ágil e prioritário para gestantes",
        "Realizar reuniões periódicas com a APS para avaliação e ajuste das ações"
    ],
    "2.5.5": [
        "Ampliar a oferta mensal de ultrassonografia obstétrica na rede municipal",
        "Garantir realização de exames dentro do período gestacional recomendado",
        "Formalizar demanda para credenciamento de serviços privados para realização de ultrassonografia obstétrica",
        "Organizar fluxo prioritário para gestantes acompanhadas no ambulatório de alto risco"
    ],
    "2.5.6": [
        "Promover educação em saúde para gestantes sobre os benefícios e segurança do parto normal",
        "Implantar grupos de preparação para o parto e nascimento nas UBS e Maternidade Municipal",
        "Capacitar profissionais da rede municipal para assistência ao parto humanizado",
        "Incentivar a atuação de enfermeiros obstetras na APS e Maternidade Municipal",
        "Fortalecer a adoção de práticas baseadas em evidências na assistência ao parto na maternidade municipal",
        "Utilizar a classificação de Robson na maternidade municipal para implementação de estratégias para redução de cesarianas",
        "Manter atualizado protocolo clínico obstétrico da maternidade municipal"
    ],
    "2.5.10": [
        "Garantir a manutenção da estrutura física adequada e ambiência da unidade",
        "Garantir a realização de ecocardiograma beira leito",
        "Garantir a realização de ultrassonografia transfontanela",
        "Assegurar funcionamento contínuo dos equipamentos e reposição quando necessário",
        "Manter quantitativo adequado de recursos humanos qualificados para assistência neonatal",
        "Promover educação permanente da equipe em neonatologia",
        "Estimular as boas práticas do método canguru",
        "Atualizar e monitorar protocolos assistenciais e de segurança do paciente",
        "Proporcionar acesso contínuo ao suporte diagnóstico e terapêutico",
        "Monitorar indicadores assistenciais (taxa de ocupação, infecção, transferências, mortalidade)",
        "Manter atualização regular dos dados no CNES",
        "Assegurar cumprimento das normas sanitárias e funcionamento da CCIH",
        "Proporcionar as triagens neonatais obrigatórias de acordo com a Orientação do ministério da Saúde (triagem metabólica, auditiva, oximetria de pulso, reflexo vermelho e o teste da linguinha)"
    ],
    "2.6.1": [
        "Realizar levantamento periódico das necessidades de materiais de consumo dos serviços da Atenção Especializada",
        "Planejar e executar processos de solicitação de demanda para a aquisição de insumos e materiais necessários ao funcionamento dos serviços",
        "Formalizar solicitação de demanda para contratação de serviços de manutenção preventiva e corretiva de equipamentos e infraestrutura",
        "Monitorar o uso e controle de estoque de materiais",
        "Garantir conformidade com normas sanitárias estabelecidas pela Agência Nacional de Vigilância Sanitária"
    ],
    "2.6.2": [
        "Realizar diagnóstico da necessidade de veículos para suporte às atividades da Atenção Especializada",
        "Planejar e formalizar solicitação de demanda para a aquisição ou locação de veículos conforme necessidade do serviço",
        "Formalizar solicitação de demanda para a manutenção preventiva e corretiva da frota existente",
        "Capacitar motoristas para transporte seguro de pacientes e equipes de saúde",
        "Assegurar conformidade com normas de transporte sanitário estabelecidas pelo Ministério da Saúde"
    ],
    "2.6.4": [
        "Realizar levantamento das necessidades de equipamentos e mobiliários dos serviços especializados",
        "Realizar levantamento da necessidade e formalizar solicitação de demanda para a aquisição de bens permanentes",
        "Acompanhar processos de compra conforme legislação vigente",
        "Instalar e disponibilizar equipamentos necessários ao funcionamento dos serviços especializados",
        "Realizar capacitação dos profissionais para utilização adequada dos equipamentos",
        "Formalizar solicitação de demanda para a manutenção preventiva e corretiva dos equipamentos adquiridos"
    ],
    "2.6.6": [
        "Ampliar o quadro de profissionais especialistas por meio de novos contratos ou credenciamentos",
        "Reorganizar e otimizar as agendas de atendimento, reduzindo o número de faltas e melhorando o aproveitamento das vagas disponíveis",
        "Realizar mutirões de consultas especializadas, priorizando especialidades com maior demanda reprimida",
        "Promover capacitação e educação permanente para profissionais, visando aprimorar a gestão de filas e o fluxo de atendimento",
        "Ampliar a oferta de especialidades médicas e serviços de apoio diagnóstico conforme perfil epidemiológico",
        "Fortalecer a articulação entre Atenção Básica e Policlínica, com protocolos de referência e contrarreferência padronizados",
        "Monitorar mensalmente os indicadores, com relatórios de consultas realizadas e taxa de absenteísmo",
        "Adequar a infraestrutura física e tecnológica da Policlínica para comportar o aumento da demanda e garantir qualidade no atendimento",
        "Desenvolver ações de comunicação e mobilização social, informando a população sobre a ampliação dos serviços e a importância do comparecimento às consultas agendadas"
    ],
    "2.6.8": [
        "Formalizar solicitação de demanda para aquisição de insumos, reagentes e equipamentos laboratoriais necessários",
        "Qualificar a equipe técnica responsável pelos exames laboratoriais",
        "Implantar protocolos de qualidade e controle dos exames",
        "Fortalecer a articulação entre Atenção Primária à Saúde e serviços laboratoriais para agilizar a coleta e entrega de resultados",
        "Monitorar indicadores de tempo de resposta e qualidade dos exames",
        "Elaborar o projeto arquitetônico conforme normas da Anvisa e da Agência Nacional de Vigilância Sanitária",
        "Articular com a APS para a informatização das UBSs com sistema laboratorial",
        "Ampliar a oferta de coletas domiciliares, reduzindo tempo de espera"
    ],
    "2.6.9": [
        "Capacitar equipes de Saúde da Família sobre rastreamento do câncer de mama e fluxos de encaminhamento",
        "Assegurar manutenção e funcionamento do mamógrafo existente, evitando paralisações por falhas técnicas",
        "Mapear a cobertura atual de mamografias por unidade de saúde e identificar áreas com menor acesso",
        "Orientar sobre atualização do cadastro de mulheres de 50 a 74 anos nas equipes de Saúde da Família",
        "Articular com a APS sobre importância de busca ativa domiciliar por ACS das mulheres que nunca realizaram mamografia",
        "Fortalecer o Outubro Rosa como mês de intensificação das ações, com metas locais de realização de exames",
        "Articular com a APS para o agendamento automático do exame para mulheres de 50 a 74 anos durante consultas na APS"
    ],
    "2.6.10": [
        "Mapear áreas com baixa cobertura e maior vulnerabilidade",
        "Assegurar fluxo adequado para encaminhamento e acompanhamento de resultados alterados",
        "Capacitar profissionais de saúde na coleta adequada do exame citopatológico",
        "Formalizar demanda para solicitação de insumos para realização desses exames",
        "Assegurar transporte adequado das lâminas para o laboratório",
        "Articular com a APS a identificação do número de mulheres na faixa etária de 25 a 64 anos por território/equipe para a realização desse exame"
    ],
    "2.6.12": [
        "Mapear e priorizar os processos assistenciais e administrativos a serem informatizados",
        "Monitorar indicadores de desempenho do sistema implantado",
        "Elaborar relatório periódico"
    ],
    "2.6.13": [
        "Acompanhar cronograma de implantação dos Protocolos Gerenciáveis e mensurá-los",
        "Monitorar os protocolos setoriais a cada 2 anos",
        "Realizar a manutenção do PAT (Programa Anual de Treinamento) vinculados aos protocolos"
    ],
    "2.6.14": [
        "Realizar as análises de 100% dos óbitos através da Comissão de Revisão de Óbito (CRO) e CMMIF (Comissão de Mortalidade Materno Infantil)",
        "Acompanhar as ações da CRO e CMMIF",
        "Assegurar a cultura multiprofissional na linha do cuidado",
        "Desenvolver o estudo de casos críticos por equipe multiprofissional"
    ],
    "2.6.15": [
        "Realizar cultura de vigilância e cultura de paciente",
        "Gerenciar o Protocolo de Higienização das mãos",
        "Desenvolver campanha de sensibilização dos profissionais para adesão do Adorno Zero no ambiente hospitalar"
    ],
    "2.6.16": [
        "Consolidar protocolos clínicos",
        "Fortalecer os POPs cirúrgicos e obstétricos para reduzir infecções hospitalares"
    ],
    "2.6.17": [
        "Consolidar a cultura de segurança do paciente, fortalecendo práticas seguras e preventivas nos processos assistenciais"
    ],
    "2.6.19": [
        "Realizar levantamento da demanda municipal de pacientes com Doença Renal Crônica (DRC) em estágio avançado e da necessidade de terapia renal substitutiva",
        "Avaliar a capacidade instalada dos serviços que realizam hemodiálise no município",
        "Ampliar a capacidade instalada de hemodiálise mediante ampliação do número de máquinas ou turnos de atendimento, conforme demanda municipal",
        "Estruturar e ofertar a modalidade de diálise peritoneal como alternativa à hemodiálise para pacientes com Doença Renal Crônica elegíveis, garantindo avaliação clínica, treinamento do paciente e acompanhamento pela equipe especializada",
        "Formalizar demanda para credenciamento ou contratação de serviços especializados para terapia renal substitutiva, conforme necessidade assistencial",
        "Fortalecer a linha de cuidado da Doença Renal Crônica no município, articulando APS, atenção especializada e serviços de TRS",
        "Organizar fluxo para realização de fístula arteriovenosa em pacientes com DRC estágio 4 e 5, que são acompanhados no Ambulatório Pré-Dialítico, antes do início da hemodiálise"
    ],
    "2.6.20": [
        "Realizar análise epidemiológica dos tipos de cânceres de maior incidência no município para planejamento de ações e serviços de saúde direcionados à prevenção, diagnóstico e tratamento do câncer",
        "Ampliar a oferta de consultas especializadas para investigação de casos suspeitos de câncer na rede própria ou contratualizada, reduzindo o tempo entre a suspeita e o diagnóstico",
        "Ampliar a oferta de exames e procedimentos diagnósticos relacionados à investigação oncológica na rede própria ou contratualizada, reduzindo o tempo entre a suspeita e o diagnóstico",
        "Ampliar a oferta de tratamento oncológico através do credenciamento ou contratação de serviços de saúde",
        "Implantar as linhas de cuidado em oncologia com definição de fluxos assistenciais entre os pontos de atenção da rede",
        "Implantar fluxos de regulação prioritária para pacientes com suspeita e diagnóstico de câncer",
        "Garantir a navegação dos pacientes dentro da rede desde a suspeita do câncer até o início do tratamento, visando reduzir o tempo de espera e garantir melhor adesão do paciente ao tratamento"
    ],
    "2.6.21": [
        "Realizar levantamento das necessidades de capacitação dos profissionais vinculados à DAES",
        "Formalizar solicitação de demanda para serviços de capacitações sobre temas relacionados à qualidade da Assistência em Saúde no município",
        "Elaborar e executar um Plano Anual de Educação Permanente, contemplando cursos, oficinas, treinamentos e atualizações técnicas voltadas à qualificação da assistência em saúde",
        "Estimular a participação dos profissionais em eventos científicos, seminários e congressos relacionados à gestão e assistência em saúde"
    ],
    "2.6.22": [
        "Realizar diagnóstico das necessidades de capacitação dos profissionais que atuam na Rede de Urgência e Emergência (SAMU, UPA, hospitais e unidades de apoio)",
        "Formalizar solicitação de demanda para contração de serviços que realizem cursos de certificação em: AMLS (Advanced Medical Life Support); ACLS (Advanced Cardiovascular Life Support); PHTLS (Prehospital Trauma Life Support); BLS (Basic Life Support) e Controle de Hemorragias e atendimento inicial ao trauma",
        "Atualizar periodicamente os protocolos de atendimento da Rede de Urgência e Emergência conforme diretrizes nacionais e internacionais",
        "Monitorar e avaliar o impacto das capacitações, analisando indicadores como tempo de resposta, qualidade do atendimento e desfechos assistenciais",
        "Manter banco de dados atualizado dos profissionais capacitados, incluindo validade das certificações"
    ],
    "3.1.1": [
        "Realizar o levantamento da capacidade instalada de oferta de cuidado na RAS (Rede própria e prestadores SUS), para contratualização de ofertas em conformidade com a nova modelagem da PNR e o Programa Agora Tem Especialista, braço da Política Nacional de Atenção Especializada em Saúde (PNAES)",
        "Elaborar Notas Técnicas de estruturação dos setores da Diretoria de Regulação Controle e Avaliação – DIRCA, em conformidade com a Nova Política de Regulação do Sistema de Saúde, compreendendo ser a regulação uma função de gestão, em seus aspectos gerenciais, administrativos, tecnológicos e clínico",
        "Publicar um ato oficial (decreto ou portaria) que institua legalmente o Núcleo de Gestão e Regulação e o Complexo Regulador Municipal (Ambulatorial e Hospitalar), cumprindo o indicador exato estabelecido para esta meta"
    ],
    "3.1.4": [
        "Realizar levantamento físico dos bens atuais e mapear o déficit de mobiliário (cadeiras ergonômicas, mesas) e tecnologia (computadores, monitores duplos) por setor",
        "Criar descritivos técnicos robustos para equipamentos de TI (servidores, headsets para regulação, nobreaks) para evitar a aquisição de materiais de baixa qualidade",
        "Garantir que cada mesa de regulação tenha dois monitores (essencial para operar o esusregulação em uma tela e prontuários/mapas em outra)",
        "Adquirir mobiliário para áreas de descanso, copa e sala de reuniões técnicas (importante para o bem-estar dos servidores que atuam em plantões de 12h/24h)",
        "Substituir 100% dos desktops antigos por máquinas com alta capacidade de processamento e armazenamento em nuvem",
        "Instalação de sistemas de climatização central e mobiliário sustentável, visando a eficiência energética do Complexo Regulador",
        "Implantar link de internet dedicado e redundante, garantindo que a regulação não pare por falta de sinal",
        "Adquirir licenças de softwares de segurança, firewalls e sistemas de backup físico/em nuvem para proteger os dados sensíveis dos pacientes"
    ],
    "3.1.5": [
        "Definir as regras de integração (APIs) para que o sistema municipal \"leia\" e \"escreva\" dados automaticamente no esus regulação (ambulatorial/hospitalar) e no e-SUS APS, evitando a digitação duplicada",
        "Especificar módulos obrigatórios: Gestão de Leitos (censo em tempo real), Gestão de Consultas/Exames, Gestão de Transporte Sanitário e Painel de Indicadores (BI)",
        "Garantir que o sistema esteja em conformidade com a LGPD (Lei Geral de Proteção de Dados), com níveis de acesso diferenciados para médicos reguladores, administrativos e gestores",
        "Instalar terminais nos hospitais para que a atualização da ocupação de leitos seja feita em tempo real, eliminando a necessidade de planilhas manuais ou ligações telefônicas constantes",
        "Realizar a transferência dos dados das filas atuais para o novo sistema, garantindo a integridade do histórico do paciente e a ordem cronológica das solicitações",
        "Treinar equipes-chave em cada UBS e Hospital para que saibam inserir solicitações com anexos (exames/laudos), reduzindo as \"devoluções\" por falta de informação"
    ],
    "3.1.6": [
        "Elaborar Matrizes de Pontuação por Especialidade, com a criação de critérios de pontuação (score) baseados em sinais, sintomas e exames para as 10 especialidades com maior fila, permitindo que o sistema classifique automaticamente em Azul, Verde, Amarelo ou Vermelho",
        "Designar uma equipe técnica de reguladores médicos para elaboração dos protocolos de classificação de risco, priorização, risco vulnerabilidade por demanda",
        "Estabelecer quais exames básicos e tratamentos prévios a APS deve realizar antes de encaminhar para a Especialidade, evitando que o especialista receba casos que poderiam ser resolvidos na UBS",
        "Padronizar os critérios de \"Vaga Zero\" e transferência prioritária entre hospitais, baseando-se em protocolos tempo-dependentes (AVC, IAM, Trauma)",
        "Realizar reuniões mensais entre médicos reguladores da DIRCA e médicos da APS para discutir casos \"devolvidos\" por falta de critério, educando a ponta sobre os novos protocolos",
        "Dar transparência à rede (APS e Hospitais) sobre qual o tempo médio de atendimento para cada cor de classificação, alinhando as expectativas do paciente",
        "Criar indicadores que mostrem quais Unidades Básicas estão encaminhando com maior precisão técnica"
    ],
    "3.1.7": [
        "Dar suporte as equipes do atual Núcleo Interno de Regulação (hospitalar) para melhorar a comunicação com o hospital geral e conveniados ao SUS",
        "Criar um grupo de trabalho com representantes da APS, DIRCA, NIRs hospitalares e o Núcleo de Gestão do Cuidado (NGC) para pactuar as responsabilidades de cada ponto da rede",
        "Desenvolver protocolos que definam o caminho exato do paciente para patologias de alto impacto (ex: Diabetes Mellitus, Hipertensão, Oncologia e Pré-natal de Alto Risco)",
        "Normatizar que o NIR é responsável pela regulação intra-hospitalar (giro de leito) e o NGC pela gestão do caso complexo (garantir que o paciente tenha suporte após a alta) e seguimento na APS após avaliação ambulatorial",
        "Estabelecer um fluxo onde o médico da APS possa tirar dúvidas com o especialista regulador via sistema antes de gerar um encaminhamento, evitando filas desnecessárias",
        "Configurar o sistema para que, no momento da internação (via NIR) ou alta, a equipe de Saúde da Família (APS) receba um alerta automático para programar a visita domiciliar",
        "Instituir gestão de cuidado e transição a partir do PLANO DE ALTA. O NGC deve validar, junto ao NIR, o plano de cuidados pós-hospitalar 24h antes da alta, enviando as orientações diretamente para a enfermeira da UBS de referência"
    ],
    "3.1.8": [
        "Criar um grupo de trabalho técnico com participação da APS e AES, para elaboração do protocolo de transição do cuidado",
        "Criar um documento técnico que defina o que deve constar obrigatoriamente no sumário de alta (diagnóstico, medicamentos prescritos, exames pendentes e orientações de sinais de alerta)",
        "Padronizar um modelo (físico ou digital) que seja entregue ao paciente e, simultaneamente, enviado à Unidade Básica de Saúde (UBS) de referência",
        "Realizar oficinas prática com profissionais da rede de atenção a saúde para utilização do mesmo",
        "Apoiar a implementação de Núcleo de Gestão do Cuidado em todas as prestadoras conveniadas ao SUS executantes das ofertas de cuidado integrado-OCI"
    ],
    "3.1.9": [
        "Criar um documento técnico que defina critérios claros (Ex: Vermelho = saída imediata; Amarelo = até 30 min; Verde = conforme agendamento) para o despacho de viaturas",
        "Instituir o protocolo via ato oficial, conferindo à Central de Regulação a autoridade para priorizar o despacho de veículos sobre agendamentos eletivos em casos de urgência",
        "Implementar um formulário único (digital ou físico padronizado) onde o médico solicitante já aponte os sinais vitais e a classificação clínica, vinculando o pedido de transporte ao código da autorização do leito",
        "Centralizar a gestão de todas as ambulâncias (eletivas e de urgência) em uma única mesa operacional, permitindo que o regulador remaneje veículos conforme a criticidade do momento",
        "Estabelecer fluxos fixos de transporte para patologias específicas, reduzindo o tempo de \"decisão\" sobre qual hospital deve receber o paciente",
        "Capacitar 100% dos motoristas, técnicos de enfermagem e reguladores sobre os novos níveis de prioridade do protocolo municipal",
        "Criar um grupo técnico para analisar mensalmente casos onde o tempo de transporte possa ter impactado o desfecho clínico, gerando melhorias no protocolo"
    ],
    "3.1.10": [
        "Criar um modelo de relatório padrão que contenha: Quantitativo por especialidade, Tempo Médio de Espera (TME), Absenteísmo (Faltas) e correlação com a oferta de prestadores",
        "Instituir um cronograma rígido para extração de dados dos sistemas reguladores (SISREG ou similar) até o 5º dia útil de cada mês, garantindo que o dado analisado seja recente",
        "Comparar mensalmente o crescimento ou redução da fila por especialidade, identificando demandas reprimidas sazonais ou falta de cobertura assistencial específica",
        "Realizar \"limpezas\" periódicas nas filas (call center ou busca ativa) para remover duplicidades, solicitações já resolvidas ou pacientes que não residem mais no município",
        "Formalizar o envio do relatório gerencial à Secretaria de Saúde e ao Conselho Municipal de Saúde, destacando as 10 especialidades com maior tempo de espera",
        "Apresentar os dados do relatório para os diretores das unidades solicitantes (UBS/UPAs) para ajustar a qualidade das guias e evitar encaminhamentos desnecessários que inflam a fila"
    ],
    "3.1.11": [
        "Elaborar protocolo que contemple as atividades de comunicação multicanal com paciente (mensagens automáticas no whatsapp, Qrcode no cartão de consulta, entre outros), para reduzir absenteísmo técnico ou institucional",
        "Promover capacitação com equipes da APS sobre utilização dos recursos do telessaúde (telerregulação assistencial)",
        "Realizar a qualificação da fila de espera com monitoramento diário pelas equipes da regulação",
        "Reduzir o absenteísmo social,atraves da designação de equipe específica para ligar para os pacientes idosos, PCD e pacientes regulados via TFD"
    ],
    "3.1.12": [
        "Desenvolver painéis de Business Intelligence (BI) que emitam alertas visuais (semáforo) quando uma solicitação atingir 80% do tempo limite previsto no protocolo",
        "Realizar reuniões breves (Daily ou Weekly) entre o médico regulador e a gestão para identificar gargalos repetitivos em patologias específicas",
        "Realizar a revisão e atualização dos Protocolos de Classificação: Atualizar as linhas de cuidado (Cardiologia, Neurologia, etc.) garantindo que os critérios de priorização estejam claros, reduzindo a subjetividade do regulador",
        "Estabelecer fluxos automáticos para patologias tempo-dependentes (como AVC e IAM), onde a autorização ocorre por critério clínico imediato, independente da confirmação imediata da logística de transporte",
        "Fortalecer os NIRs nos hospitais executores para acelerar a liberação de leitos ociosos e a comunicação imediata da vacância à Central de Regulação",
        "Implementar ou ampliar o Serviço de Atenção Domiciliar (SAD) para pacientes de baixa complexidade, liberando leitos hospitalares para as solicitações da regulação",
        "Capacitar 100% da equipe de regulação nos protocolos vigentes para evitar reiterações (pedidos de mais informações) que travam o relógio da autorização"
    ],
    "3.1.13": [
        "Posicionar ambulâncias de suporte em pontos estratégicos (nós de rede) para reduzir o \"tempo de deslocamento em vazio\" até o paciente",
        "Estabelecer um sistema de rodízio e manutenção que garanta que 95% da frota de transporte prioritário esteja operacional 24/7, evitando baixas inesperadas",
        "Criar protocolos de higienização rápida (pós-transporte) para que o veículo retorne ao status de \"disponível\" no menor tempo possível",
        "Instalar ou atualizar sistemas de telemetria em 100% da frota para que a Central de Regulação visualize a viatura mais próxima da ocorrência prioritária",
        "Automatizar a escala de motoristas e técnicos para garantir que não haja \"vazio assistencial\" por falta de pessoal qualificado no momento do chamado",
        "Estabelecer uma \"via rápida\" no rádio/sistema para chamados classificados como urgentes, com tempo de saída da base em no máximo 10 minutos após o chamado",
        "Treinar 100% dos condutores em protocolos de transporte de pacientes críticos e fluxos de comunicação via rádio",
        "Formalizar parcerias com municípios vizinhos ou consórcios de saúde para suporte em casos de picos de demanda que excedam a capacidade local",
        "Assegurar o acesso de pessoas com deficiências físicas, auditivas, intelectuais, visuais ou múltiplas aos pontos de atenção, através de transporte sanitário adpatado"
    ],
    "3.1.14": [
        "Realizar o levantamento de Necessidades de Aprendizagem (LNA), com aplicação de questionários anuais aos reguladores e equipes da APS e EAS para identificar as maiores dificuldades (ex: preenchimento de laudos, uso do sistema, critérios de priorização)",
        "Realizar a atualização de protocolos específicos das especialidades",
        "Realizar ciclos de oficinas formativas práticas (encontros presenciais e a distancia)"
    ],
    "3.1.15": [
        "Padronizar \"Checklists de Conformidade\" para os procedimentos de maior custo e volume (ex: Cirurgias Eletivas, Exames de Alta Complexidade), garantindo que todos os auditores avaliem os mesmos critérios",
        "Estabelecer a rotina de conferência obrigatória de uma amostra (ex: 10% a 20%) das Autorizações de Internação Hospitalar (AIH) e Boletins de Produção Ambulatorial (BPA) antes da aprovação do pagamento",
        "Realizar treinamento focado em faturamento SUS, codificação de procedimentos (SIGTAP) e preenchimento de laudos médicos para reduzir glosas por erros formais",
        "Instituir a presença física ou virtual do auditor nos hospitais durante a internação do paciente, validando a necessidade do procedimento e a qualidade da assistência enquanto ela ocorre",
        "Elaborar relatórios com devolutivas às prestadoras de saúde e rede própria",
        "Integrar ao sistema de regulação alertas para \"Inconsistências de Faturamento\" (ex: cobrança de procedimentos incompatíveis com a idade ou sexo do paciente, ou excesso de exames para um mesmo diagnóstico)",
        "Estruturar um Dashboard que mostre o índice de aprovação e reprovação de faturas por prestador, permitindo que a gestão identifique quais unidades precisam de intervenção ou reorientação técnica",
        "Implementar busca ativa (telefônica ou digital) para confirmar com o paciente se o procedimento faturado pelo prestador foi efetivamente realizado e se a qualidade foi adequada"
    ],
    "3.1.16": [
        "Fortalecer equipe de análise de produção (rede conveniada e MAC)",
        "Treinar equipe de auditoria, controle e avaliação",
        "Revisar rotinas de envio de dados",
        "Realizar capacitações com prestadores do SUS sobre registro e consolidação de informações (rede conveniada e MAC)"
    ],
    "3.1.17": [
        "Elaborar o Protocolo Municipal do TFD e posterior publicação de Portaria",
        "Criar um guia prático que defina quem tem direito, quais documentos são obrigatórios e os prazos máximos para cada etapa (análise médica, autorização administrativa e agendamento de transporte/ajuda de custo)",
        "Realizar o treinamento das unidades (APS, AES) sobre o novo fluxo",
        "Disponibilizar para as UBS e Hospitais um check-list rigoroso para que o processo já chegue à regulação completo, evitando \"diligências\" que travam o prazo de análise",
        "Centralizar o recebimento das solicitações para evitar a dispersão de documentos e permitir o protocolo imediato com número de rastreio para o paciente",
        "Implementar a informatização dos processos de TFD, integrando as solicitações ao sistema de regulação municipal, permitindo que o paciente acompanhe o status (análise, autorizado, aguardando transporte) via terminal ou aplicativo",
        "Criar um painel gerencial que aponte alertas vermelhos para processos que estejam chegando ao limite do prazo estabelecido no protocolo municipal (Ex: 5 dias para análise prioritária)",
        "Revisar os contratos de passagens, garantindo que o fator financeiro/logístico não atrase o encaminhamento do paciente já autorizado e as ajudas de custo sejam liberadas em tempo hábil",
        "Realizar relatórios trimestrais que cruzem os dados do TFD com o perfil epidemiológico do município, identificando se as autorizações estão atendendo às áreas de maior vulnerabilidade e necessidade clínica",
        "Formalizar o grupo de médicos reguladores responsáveis pela análise clínica do TFD, estabelecendo metas semanais de vazão de processos acumulados"
    ],
    "3.1.18": [
        "Realizar treinamento inicial sobre o PMAE e a nova modalidade de cuidado na atenção especializada, no primeiro quadrimestre de 2026, com 100% dos médicos generalistas das UBS's",
        "Implantar as OCI's de Otorrinolaringologia e Oftalmologia até a 2º quadrimestre de 2026",
        "Implantar as demais OCI's pactuadas até o final do 3º quadrimestre de 2029",
        "Criar indicadores de processo na implantação das OCI'S, a serem acompanhados pelo Núcleo de Gestão e Regulação (Indicadores de Integração e Governança, Indicadores de Fluxo e Tempestividade e Indicadores de Qualidade da Informação/Continuidade)"
    ],
    "3.1.19": [
        "Criar um Grupo de Trabalho Interno na Regulação para revisão diária de dados cadastrais e solicitações",
        "Elaborar o Procedimento Operacional Padrão (POP) de triagem e revisão clínica das solicitações vindas das Unidades básicas de saúde",
        "Desenvolver um protocolo de suspensão administrativa, a partir da normatização de solicitações que estejam sem atualização de exames ou contato há mais de 12 meses sejam movidas para uma \"fila de contingência\" até que o paciente compareça à UBS para reavaliação",
        "Responsabilizar as equipes de Estratégia de Saúde da Família (ESF) pela atualização bianual das condições clínicas dos seus pacientes que estão na fila de cirurgia, inserindo as notas diretamente no prontuário integrado",
        "Desenvolver um Dashboard que aponte automaticamente registros que não sofrem interação do regulador há mais de 90 dias, gerando um alerta de \"necessidade de depuração\"",
        "Analisar as causas das faltas no dia da cirurgia. Se o motivo for \"paciente já operado\" ou \"desistência\", retroagir no processo para identificar por que a depuração falhou naquele caso específico"
    ],
    "4.1.1": [
        "Articular junto as diretorias a indicação dos membros para compor a equipe multidisciplinar da CFT",
        "Elaborar e publicar Portaria Municipal de instituição da CFT com as devidas atribuições dos membros",
        "Elaborar e aprovar o Regimento Interno da CFT",
        "Realizar oficina de capacitação dos membros da CFT",
        "Planejar as atividades e cronograma das reuniões da CFT",
        "Monitorar e avaliar o desempenho da CFT, garantindo periodicidade das reuniões, cumprimento de pautas e atualização regular da REMUME"
    ],
    "4.1.2": [
        "Realizar análise do perfil epidemiológico e do consumo de medicamentos",
        "Realizar alinhamento técnico com a RENAME 2024 e protocolos clínicos vigentes",
        "Realizar a elaboração da versão oficial da REMUME",
        "Realizar a validação da REMUME junto a CMS e publicação no Diário Oficial e Portais oficiais",
        "Realizar uma ampla divulgação da REMUME junto aos profissionais de saúde e a população",
        "Realizar a atualização da REMUME a cada 2 anos ou de acordo com a versão atualizada da RENAME"
    ],
    "4.1.3": [
        "Realizar o Ciclo da Assistência Farmacêutica (Seleção, Programação, Aquisição, Armazenamento e Distribuição/ Dispensação)",
        "Monitorar quinzenalmente o sistema de gerenciamento e informações (HÓRUS)",
        "Monitorar os repasses tripartite para Assistência Farmacêutica de acordo com as portarias do Ministério da Saúde e Comissão Intergestores Bipartite – CIB e Comissão Intergestores Regional – CIR",
        "Divulgar quinzenalmente no site da prefeitura e outras mídias digitais os estoques de medicamentos das farmácias do SUS",
        "Capacitar farmacêuticos e auxiliares de farmácia em boas práticas de armazenamento, controle de validade e dispensação racional de medicamentos",
        "Fortalecer a integração entre a Assistência Farmacêutica e as equipes de Atenção Primária à Saúde (APS), visando o uso racional de medicamentos e a otimização da logística de reposição",
        "Promover reuniões periódicas entre a Diretoria/Gerencias da Assistência Farmacêutica com a Diretoria Administrativa/setor de Compras para alinhamento sobre cronogramas licitatórios e contratos",
        "Planejar, participar e monitorar os processos licitatórios com base em dados atualizados de consumo, evitando descontinuidade no fornecimento por atrasos ou falhas contratuais"
    ],
    "4.1.4": [
        "Realizar a padronização dos medicamentos de acordo protocolos clínicos e terapêuticos implantados pelas CFT nos serviços especializados da MAC e urgência/emergência",
        "Realizar aquisição e distribuição de medicamentos e insumo de acordo com a padronização aprovada pela CFT para os serviços especializados da MAC e urgência/emergência",
        "Realizar articulação com a DAES para funcionamento 24 horas da farmácia da Unidade de Pronto Atendimento – UPA",
        "Realizar articulação com a DAES para implantação da dispensação individualizada na Unidade de Pronto Atendimento – UPA",
        "Monitorar quinzenalmente o sistema de gerenciamento e informações (HÓRUS)",
        "Planejar e monitorar os processos licitatórios com base em dados atualizados de consumo, evitando descontinuidade no fornecimento por atrasos ou falhas contratuais"
    ],
    "4.1.5": [
        "Realizar a atualização do cadastro das crianças beneficiárias do Programa APLV, garantindo informações completas sobre diagnóstico, idade, fórmula prescrita, unidade de acompanhamento e período de tratamento",
        "Solicitar inclusão do Programa de Saúde APLV no Sistema Hórus Básico ao DataSUS",
        "Monitorar mensalmente a demanda e o consumo médio das fórmulas, utilizando essas informações para subsidiar o planejamento de compras e prevenir desabastecimentos",
        "Planejar e monitorar os processos licitatórios com base em dados atualizados de consumo, evitando descontinuidade no fornecimento por atrasos ou falhas contratuais",
        "Estabelecer fluxo de comunicação entre a CAF e responsável pelo programa na APS, para informar sobre entregas, estoques e eventuais atrasos no fornecimento",
        "Realizar articulação junto a CIR/ CIB para regulamentação das competências do financiamento das fórmulas incorporadas pela CONITEC"
    ],
    "4.1.6": [
        "Atualizar o cadastro dos usuários beneficiários do Programa de Fornecimento de Fraldas para garantir a aquisição e fornecimento em quantidades de acordo com protocolo municipal",
        "Solicitar inclusão do Programa de Saúde Fraldas no Sistema Hórus Básico ao DataSUS",
        "Monitorar mensalmente a demanda e o consumo médio das fraldas, utilizando essas informações para subsidiar o planejamento de compras e prevenir desabastecimentos",
        "Planejar e monitorar os processos licitatórios com base em dados atualizados de consumo, evitando descontinuidade no fornecimento por atrasos ou falhas contratuais",
        "Estabelecer fluxo de comunicação entre a CAF e as UBS, para informar sobre entregas, estoques e eventuais atrasos no fornecimento",
        "Realizar articulação junto a CIR/CIB para regulamentação das competências do financiamento das fraldas"
    ],
    "4.1.7": [
        "Elaborar projeto técnico para implantação da Farmácia Viva, contemplando cultivo, beneficiamento e dispensação de plantas medicinais, conforme diretrizes do edital de chamamento público do processo seletivo de projetos para implantação e/ou estruturação de farmácias vivas da SECTICS/MS",
        "Constituir grupo de trabalho intersetorial (Assistência Farmacêutica, Atenção Básica, Vigilância Sanitária e Agricultura) para coordenar as ações da Farmácia Viva e o uso de fitoterápicos",
        "Selecionar plantas a serem cultivadas e manipuladas",
        "Firmar parcerias de cooperação técnica com as Instituições acadêmicas (Universidades e Escolas Técnicas)",
        "Selecionar duas opções de fitoterápicos da RENAME vigente, com base nas condições de saúde mais prevalentes na APS e nos protocolos do Ministério da Saúde",
        "Capacitar profissionais da APS e farmacêuticos sobre uso racional de fitoterápicos e plantas medicinais, segurança, indicações terapêuticas e manejo clínico integrado",
        "Elaborar cartilha de orientações técnicas municipais para prescrição de plantas medicinais e fitoterápicos, com base no Memento Fitoterápico da ANVISA"
    ],
    "4.1.8": [
        "Realizar diagnóstico situacional das unidades de saúde e farmácias do SUS municipal, identificando o quantitativo de farmacêuticos, lacunas de cobertura e demandas prioritárias",
        "Articular elaboração do plano de provimento e lotação de farmacêuticos, considerando critérios técnicos e o cumprimento da Lei nº 13.021/2014, que assegura a presença do profissional responsável técnico em todas as farmácias",
        "Articular a inserção de farmacêuticos nos processos seletivos ou concursos públicos, conforme a necessidade identificada no diagnóstico",
        "Capacitar farmacêuticos nas áreas de gestão da AF, incluindo programação, aquisição, controle de estoques, sistemas de informação (Hórus) e indicadores de desempenho",
        "Implantar rotina de reuniões técnicas entre farmacêuticos e a diretoria/gerencias da AF, para acompanhamento dos processos de aquisição, distribuição, cuidado farmacêutico e monitoramento do acesso e do uso racional de medicamentos",
        "Incluir os farmacêuticos nas comissões técnicas do município, fortalecendo sua atuação estratégica",
        "Implantar ações de cuidado farmacêutico nas UBS, priorizando acompanhamento de pacientes com doenças crônicas (hipertensão, diabetes, asma, dislipidemia)",
        "Promover ações sobre uso racional de medicamentos com profissionais da APS e comunidade"
    ],
    "4.1.9": [
        "Implantar legalmente a Diretoria de Assistência Farmacêutica no município (Lei, Decreto Municipal e outros)",
        "Normatizar o funcionamento da CAF e das farmácias dos serviços SUS com a aquisição dos documentos legais de funcionamento e documentos padrões operacionais. (Alvará Sanitário e Certidão de Regularidade Técnica, POPs)",
        "Realizar alimentação sistemática do sistema de gerenciamento para manutenção do custeio do QUALIFARSUS (HÓRUS/ESUS AF) com envio dos dados da AF local para Base Nacional (BNAFAR)",
        "Prover a execução e manutenção do Programa QUALIFARSUS no município",
        "Realizar aquisição de equipamentos e mobiliários necessários para estruturação da CAF e das farmácias do SUS",
        "Realizar articulação para oferecer educação permanente como cursos presenciais, EAD de qualificações para os profissionais da AF, na lógica das Redes de Atenção à Saúde (curso, seminários, pós graduações Lato Sensu e outros.)",
        "Inserir o profissional farmacêutico nas práticas clinicas dos serviços de saúde com foco na melhoria da resolutividade das ações em saúde, otimizando benefício ao usuário e minimizando os riscos relacionados à farmacoterapia",
        "Realizar articulação para a inserção do profissional farmacêutico nas equipes multiprofissional (eMult) da APS"
    ],
    "4.1.11": [
        "Prover a efetivação do Sistema Nacional de Gestão da Assistência Farmacêutica do SUS – HÓRUS na CAF com seu funcionamento integral e efetivo",
        "Descentralizar o sistema HÓRUS para as farmácias de serviços SUS melhorando a transmissão das informações para Base Nacional de Dados de Ações e Serviços da Assistência Farmacêutica – BNAFAR",
        "Realizar manutenção dos equipamentos de informática e conectividade necessária para execução do Sistema HÓRUS nos serviços",
        "Realizar cadastro e treinamento dos profissionais das farmácias para manuseio do HÓRUS"
    ],
    "4.1.12": [
        "Articular a criação do fluxo administrativo de Solução de Conflitos para receber as solicitações da população, analisar tecnicamente em curto prazo (7 a 15 dias) e propor soluções técnica e célere com foco em evitar a judicialização",
        "Articular a instituição e formalização da Câmara Administrativa de Solução de Conflitos (portaria municipal instituindo o fluxo administrativo e comissão técnica",
        "Formalizar canal técnico e coordenação interfederativa permanente com a Assistência Farmacêutica Estadual criando em conjunto um grupo formal de comunicação institucional para diagnostico situacional das judicializações, discussão e proposições de cooperação que permita antecipar desabastecimento e possíveis judicializações",
        "Supervisionar os processos de pacientes cadastrados no Unidade de Dispensação de Medicamentos Especializados - UDME no município para a aquisição dos medicamentos especializados de alto custo de responsabilidade do MS e SES, com produção de planilha mensal de monitoramento de desabastecimento e impacto financeiro municipal",
        "Emitir relatórios técnicos (assinados pelo responsável farmacêutico e financeiro) documentando medicamentos de competência estadual judicializados e o custo assumido pelo município encaminhando para diretoria jurídica, anexando ainda, nas reuniões da CIR (Comissão Intergestores Regional) para ciência e providencias",
        "Propor na CIR e CIB a criação de um Fluxo de Responsabilidade Compartilhada, fluxo que defina como o município deve proceder em caso de ausência temporária do Estado (prazos de reposição, substituição temporária, reembolso, comunicação de urgência) evitando disputas e judicializações que recaiam injustamente sobre o município",
        "Registrar formalmente a ausência estadual (ofício técnico) e comunicar ao Judiciário/MP/procuradoria/defensoria local sempre que houver falta prolongada de medicamento estadual, informando a situação e anexando evidências (notas fiscais, ofícios, respostas do Estado)",
        "Elaborar fluxograma de integração entre Ouvidoria e Assistência Farmacêutica"
    ],
    "4.1.13": [
        "Implantar pontos de coleta padronizados nas farmácias das Unidades Básicas de Saúde (UBS), na UPA, e em demais serviços municipais de saúde",
        "Estabelecer fluxo interno de recolhimento e transporte dos medicamentos descartados para a Central de Abastecimento Farmacêutica (CAF)",
        "Firmar parceria com empresa licenciada para tratamento e destinação final de resíduos farmacêuticos",
        "Capacitar os profissionais das unidades sobre procedimentos corretos de segregação, armazenamento temporário e registro dos resíduos",
        "Desenvolver ações educativas junto aos usuários sobre o descarte seguro de medicamentos domiciliares",
        "Monitorar e registrar os quantitativos coletados, o destino final e os relatórios de conformidade ambiental"
    ],
    "5.1.1": [
        "Realizar levantamentos entomológicos regulares para identificação de espécies de anofelinos e para mapear áreas de transmissão ativa e priorizar ações",
        "Ampliar testagem e supervisão de tratamento",
        "Assegurar acesso gratuito e imediato à medicação, conforme o esquema terapêutico preconizado",
        "Desenvolver campanhas educativas sobre sinais e sintomas da malária e importância do diagnóstico precoce",
        "Realizar parcerias com lideranças comunitárias, escolas e associações locais para promoção de vigilância participativa",
        "Implementar e atualizar anualmente o Plano Municipal de Enfrentamento da Malária"
    ],
    "5.1.2": [
        "Realizar ações extramuros de testagens realizadas pelo CTA/SAE",
        "Realizar ações voltadas para os grupos de maior vulnerabilidade e risco para o HIV/AIDS",
        "Aumentar a oferta de autoteste para os usuários que utilizam PREP",
        "Acompanhar os pacientes com HIV/AIDS diagnosticados no Hospital Geral de Parauapebas referenciados aos CTA/SAE"
    ],
    "5.1.3": [
        "Fornecer testagem rápida para HIV no pré-natal em todas as gestantes em todas as UBS",
        "Acompanhar gestantes com HIV no SAE",
        "Acompanhar crianças expostas com HIV no SAE",
        "Acompanhar parturientes referenciadas pela Maternidade Municipal no SAE",
        "Capacitar equipes da APS, hospitalar e maternidades sobre prevenção da transmissão vertical e manejo clínico"
    ],
    "5.1.4": [
        "Acompanhar rotineiramente os indicadores de exames de contatos",
        "Identificar UBS com baixos percentuais e planejar intervenções direcionadas",
        "Enviar boletins mensais de acompanhamento de pacientes às equipes da APS",
        "Realizar monitoramento mensal do SINAN para garantir registros completos e corretos",
        "Realizar visitas técnicas de supervisão nas UBS",
        "Apoiar a APS na organização de campanhas educativas sobre prevenção e diagnóstico precoce da TB e mutirões para exame de contatos",
        "Realizar capacitações periódicas aos profissionais sobre fluxos e protocolos do programa de TB",
        "Articular com a gestão sobre a falta de insumos para a vigilância de contatos"
    ],
    "5.1.5": [
        "Prover testagem rápida de sífilis em todas as gestantes no 1º trimestre, com repetição no 3º trimestre",
        "Monitorar a testagem rápida no momento do parto",
        "Monitorar as titulações de VDRL durante a gestação",
        "Realizar ações educativas e campanhas intersetoriais de prevenção e conscientização",
        "Treinar profissionais da assistência ao pré natal e rede hospitalar sobre classificação e tratamento adequados e em tempo oportuno em parceria com a Rede Alyne",
        "Sensibilizar sobre a importância da adesão ao tratamento pelos parceiros",
        "Monitorar o registro do tratamento realizado pelas gestantes incentivando a referência e contrarreferência entre APS, APGAR e Maternidade"
    ],
    "5.1.6": [
        "Incentivar microplanejamento das ações de imunização na APS, priorizando áreas com baixa cobertura e maior vulnerabilidade",
        "Realizar rotina mensal de monitoramento das coberturas vacinais por UBS",
        "Adquirir estoque adequado e contínuo de imunobiológicos e insumos (seringas, cartões, caixas térmicas)",
        "Promover campanhas municipais e Dias D de vacinação com apoio intersetorial",
        "Fortalecer a integração APS/Vigilância para busca e acompanhamento de faltosos",
        "Realizar visitas técnicas em todas as salas de vacina do município",
        "Capacitar sistematicamente vacinadores e técnicos de sala de vacina sobre boas práticas e registro no SIPNI e e-SUS APS (PEC)",
        "Intensificar ações de comunicação social e combate à desinformação vacinal (redes sociais, escolas, rádios)",
        "Disponibilizar veículo e apoio operacional durante as ações de campo e campanhas"
    ],
    "5.1.7": [
        "Elaborar e executar Plano de Capacitação para Notificação de Violências, com cronograma anual abrangendo APS, hospitais e serviços privados",
        "Promover oficinas intersetoriais com participação de CRAS, CREAS, Conselho Tutelar, Educação e Segurança Pública",
        "Capacitar notificadores (médicos, enfermeiros, psicólogos, assistentes sociais) sobre uso da Ficha de Notificação Individual",
        "Divulgar materiais técnicos e fluxogramas simplificados para identificação e encaminhamento de casos de violência",
        "Realizar campanhas temáticas com outros setores (SEMMU, SEMAS) com enfoque na prevenção e na notificação obrigatória",
        "Implantar painel de monitoramento de notificações de violências com indicadores quadrimestrais por tipo de violência e faixa etária"
    ],
    "5.1.8": [
        "Acompanhar rotineiramente os indicadores de exames de contatos",
        "Identificar UBS com baixos percentuais e planejar intervenções direcionadas",
        "Enviar boletins mensais de acompanhamento de pacientes às equipes da APS",
        "Realizar monitoramento mensal do SINAN para garantir registros completos e corretos",
        "Realizar visitas técnicas de supervisão nas UBS",
        "Apoiar a APS na organização de campanhas educativas sobre prevenção e diagnóstico precoce da hanseníase e mutirões para exame de contatos",
        "Realizar capacitações periódicas aos profissionais sobre fluxos e protocolos do programa de hanseníase"
    ],
    "5.1.9": [
        "Elaborar Plano Anual de Ações Educativas da Vigilância Sanitária, com metas e cronograma",
        "Desenvolver campanhas temáticas mensais (boas práticas de manipulação, alimentos, medicamentos, serviços de saúde, água, resíduos, estética, escolas, entre outros)",
        "Promover palestras, rodas de conversa e oficinas educativas em escolas, feiras livres, indústrias e estabelecimentos de saúde",
        "Produzir materiais educativos padronizados e acessíveis (folders, banners, vídeos e cartilhas digitais)",
        "Prover o aumento de pessoal para realização das ações",
        "Criar indicador de desempenho interno com devolutiva bimestral às equipes",
        "Realizar mostra municipal de boas práticas em vigilância sanitária educativa ao final do quadriênio"
    ],
    "5.1.10": [
        "Realizar oficinas de formação para registro das fichas/formulários de notificações de acidentes e doenças relacionadas ao trabalho",
        "Produção e distribuição de materiais informativos para os trabalhadores e população em geral",
        "Realizar monitoramento com devolutiva sistemática nas unidades sobre os registros das notificações",
        "Estabelecer painel municipal de agravos relacionados ao trabalho com indicadores e evolução histórica"
    ],
    "5.1.13": [
        "Firmar contratos contínuos de manutenção para os equipamentos e veículos da Vigilância em Saúde",
        "Informatizar o almoxarifado específico da Vigilância em Saúde"
    ],
    "5.1.14": [
        "Priorizar a aquisição de equipamentos de tecnologia da informação (computadores, tablets, smartphones) para as equipes de campo e de retaguarda da Vigilância",
        "Direcionar parte das aquisições para a renovação das câmaras de conservação de imunobiológicos (Rede de Frio) e para o parque tecnológico do Laboratório de Saúde Pública/CTA"
    ],
    "5.1.15": [
        "Elaborar projetos técnicos e submetê-los ao Ministério da Saúde para captação de recursos via emendas ou programas federais, desonerando o Tesouro Municipal"
    ],
    "5.1.17": [
        "Determinar que os relatórios das investigações dos óbitos sejam encaminhados obrigatoriamente aos grupos condutores da Rede Alyne, para adequação imediata dos fluxos de urgência obstétrica e do Ambulatório de Gestação de Alto Risco (AGPAR)",
        "Instituir uma portaria local que determine prazos rigorosos para a equipe de vigilância: toda investigação de morte materna de residente deve ser concluída e digitada no SIM no prazo máximo de 60 dias após o óbito, garantindo o alcance das metas de repasse federal do PQA-VS",
        "Realizar capacitação contínua dos médicos do Hospital Geral de Parauapebas (HGP) e hospitais privados para o correto preenchimento da Declaração de Óbito (DO), mitigando o uso de causas mal definidas (\"Códigos Garbage\") e permitindo a identificação exata das mortes ligadas ao ciclo gravídico-puerperal",
        "Sempre que o Comitê e a Vigilância concluírem a investigação de um óbito materno evitável, a Unidade Básica de Saúde (UBS) de origem da paciente deverá ser notificada para que a equipe de Saúde da Família promova uma discussão de caso interno, revisando as falhas cometidas no pré-natal local (ex: falta de exames de sífilis, subestimação de hipertensão)"
    ],
    "5.1.18": [
        "Garantir logística para que a equipe de vigilância realize entrevistas domiciliares e hospitalares (Autópsia Social/Verbal)",
        "Instituir Fluxo Operacional Padrão (POP) estabelecendo que toda investigação de óbito infantil e fetal seja concluída e digitada no SIM em até 60 dias",
        "Estabelecer que, para cada óbito infantil/fetal considerado \"evitável\" por falha no pré-natal, a Unidade Básica de Saúde (UBS) responsável seja notificada",
        "Treinar anualmente os médicos do Hospital Geral de Parauapebas, do Serviço de Verificação de Óbitos (SVO) e das maternidades conveniadas"
    ],
    "5.1.19": [
        "Instituir a obrigatoriedade de prestação de contas dos Núcleos Hospitalares de Epidemiologia (NHE) ao Comitê",
        "Criar o fluxo do \"Alerta Assistencial\""
    ],
    "5.1.20": [
        "Treinar equipes da Atenção Primária e Hospitais para eliminar campos \"em branco\" nas fichas de notificação do SINAN",
        "Evitar o desabastecimento de testes rápidos e vacinas vinculados às metas do PQA-VS",
        "Estabelecer fluxos de investigação rápida de óbitos suspeitos de Dengue e Chikungunya"
    ],
    "6.1.1": [
        "Atender as condicionantes para obtenção e renovação das licenças (sanitária, ambiental, de funcionamento e do Corpo de Bombeiros), por meio de intervenções estruturais, correções sanitárias, atualização de projetos técnicos e organização documental",
        "Melhorar ou estruturar a operacionalização do manejo, segregação, acondicionamento, coleta, transporte, tratamento e destinação final ambientalmente adequada dos resíduos em todas as unidades de saúde",
        "Implantar a coleta seletiva com a segregação de resíduos comuns recicláveis, com disponibilização de recipientes adequados, definição de fluxos internos e articulação com sistemas de coleta e destinação",
        "Implementar rotinas de acompanhamento, controle de prazos das licenças, auditorias internas e capacitação das equipes para garantir a manutenção da regularização e conformidade com a legislação vigente"
    ],
    "6.1.3": [
        "Estabelecer um cronograma anual consolidado para licitações e aquisições de materiais de consumo, utilizando o histórico de consumo das unidades para evitar rupturas de estoque",
        "Instituir rotinas rigorosas de fiscalização e execução de contratos de manutenção preventiva e corretiva (predial, frota e equipamentos médico-hospitalares) em toda a rede",
        "Implementar um sistema informatizado de gestão logística integrada que monitore em tempo real os níveis de estoque em cada unidade de saúde, estabelecendo alertas automáticos de estoque mínimo e prazos de validade para assegurar a reposição programada sem interrupções na assistência"
    ],
    "6.1.4": [
        "Realizar um levantamento contínuo das necessidades de mobiliários, equipamentos de informática e aparelhos médico-hospitalares em cada unidade ou setor administrativo",
        "Executar os trâmites de compra e distribuição desses bens permanentes, garantindo que as equipes tenham a estrutura necessária para realizar suas atividades",
        "Acompanhar o avanço do \"Percentual de serviços da SEMSA com equipamentos adequados\""
    ],
    "6.1.5": [
        "Instituir um cronograma obrigatório para que todas as unidades de saúde relatem equipamentos, macas, computadores e mobiliários quebrados ou obsoletos",
        "Estruturar o processo administrativo para realizar o leilão público dos itens que ainda possuem valor de sucata ou providenciar o descarte ecológico adequado, visando cumprir o indicador de 100% dos bens inservíveis inventariados a cada ano"
    ],
    "6.1.6": [
        "Realizar levantamentos e vistorias periódicas para identificar com exatidão as necessidades estruturais (hidráulicas, elétricas e civis) de cada unidade de saúde",
        "Estruturar e executar um plano contínuo de manutenção preventiva e corretiva, evitando interrupções nos atendimentos por falhas na infraestrutura",
        "Realizar as obras necessárias para que os prédios cumpram as normas sanitárias e de acessibilidade vigentes, garantindo um ambiente seguro e acolhedor"
    ],
    "6.1.7": [
        "Avaliar rigorosamente as unidades de saúde que atualmente funcionam em prédios alugados no município, verificando se continuam atendendo às exigências sanitárias, técnicas e de segurança",
        "Exigir laudos técnicos (de engenharia, acessibilidade e vigilância sanitária) antes de assinar ou renovar qualquer contrato de locação, assegurando que a infraestrutura do imóvel suporta os serviços de saúde que serão prestados",
        "Instituir um fluxo administrativo para planejar e renovar anualmente os contratos com antecedência, evitando o vencimento, multas ou a interrupção dos atendimentos à população"
    ],
    "6.1.8": [
        "Mapear a demanda real de transporte (para pacientes, equipes de saúde e setor administrativo) e realizar a aquisição ou locação de veículos para suprir as deficiências da frota atual",
        "Executar cronogramas contínuos de manutenção preventiva e corretiva para todos os veículos, minimizando o tempo de frota parada e garantindo a segurança de motoristas e passageiros",
        "Implementar um controle centralizado de rotas, consumo de combustível e agendamento de viagens, otimizando o uso diário dos veículos em todos os pontos da rede"
    ],
    "6.1.9": [
        "Realizar um levantamento de todos os fluxos de trabalho nos setores prioritários da secretaria (como planejamento, regulação, assistência farmacêutica e recursos humanos), identificando gargalos, retrabalhos e etapas desnecessárias",
        "Desenvolver e documentar Manuais Técnico-Normativos e POPs para cada rotina administrativa e assistencial. A padronização garante que as tarefas sejam executadas com a mesma qualidade e eficiência, independentemente de mudanças na equipe, minimizando erros e desperdícios",
        "Validar e publicar oficialmente esses novos fluxos e manuais por meio de atos normativos (portarias ou resoluções internas). Isso assegura o respaldo legal para a atuação dos servidores e garante a transparência exigida na gestão pública"
    ],
    "6.1.10": [
        "Implantar um sistema informatizado (Help Desk) para registrar, categorizar e rastrear todas as solicitações administrativas (como suporte de TI, RH e suprimentos) feitas pelas unidades de saúde ao nível central",
        "Estabelecer tempos máximos de resposta e resolução para cada tipo de demanda, garantindo que as unidades da ponta não fiquem desassistidas",
        "Treinar os servidores administrativos para executarem suas funções com base nas rotinas que foram padronizadas, reduzindo erros, burocracia e retrabalho"
    ],
    "6.2.1": [
        "Garantir a coleta, validação e consolidação de 100% dos dados necessários à elaboração da PMS junto às áreas técnicas da Secretaria de Saúde",
        "Elaborar e registrar integralmente o Plano Municipal de Saúde (PMS) no DigiSUS Gestor dentro do prazo estabelecido pelo Ministério da Saúde",
        "Submeter o PMS à análise e deliberação do Conselho Municipal de Saúde, garantindo apreciação e resolução",
        "Realizar a revisão periódica das metas do Plano Municipal de Saúde (PMS), promovendo ajustes, inclusões ou exclusões quando necessário, com base nos resultados dos indicadores, relatórios quadrimestrais e mudanças no cenário epidemiológico, submetendo as alterações à análise e deliberação do Conselho Municipal de Saúde"
    ],
    "6.2.2": [
        "Garantir a coleta, validação e consolidação de 100% dos dados necessários à elaboração da PAS junto às áreas técnicas da Secretaria de Saúde",
        "Elaborar e registrar integralmente a Programação Anual de Saúde (PAS) no DigiSUS Gestor dentro do prazo estabelecido pelo Ministério da Saúde",
        "Submeter a PAS à análise e deliberação do Conselho Municipal de Saúde, garantindo apreciação e resolução"
    ],
    "6.2.3": [
        "Garantir a coleta, validação e consolidação de 100% dos dados quadrimestrais necessários à elaboração do RDQA junto às áreas técnicas da Secretaria de Saúde",
        "Elaborar e registrar integralmente o Relatório Detalhado do Quadrimestre Anterior (RDQA) no DigiSUS Gestor dentro do prazo estabelecido pelo Ministério da Saúde",
        "Submeter o RDQA à análise e deliberação do Conselho Municipal de Saúde, garantindo apreciação e resolução"
    ],
    "6.2.4": [
        "Garantir a coleta, validação e consolidação de 100% dos dados necessários à elaboração do RAG junto às áreas técnicas da Secretaria de Saúde",
        "Elaborar e registrar integralmente o Relatório Anual de Gestão (RAG) no DigiSUS Gestor dentro do prazo estabelecido pelo Ministério da Saúde",
        "Submeter o RAG à análise e deliberação do Conselho Municipal de Saúde, garantindo apreciação e resolução"
    ],
    "6.2.5": [
        "Criar normativa interna definindo o cronograma rigoroso de repasse de dados pelas diretorias técnicas para a Diretoria de Planejamento. Para inserção dos instrumentos no sistema DigiSUS (maio, setembro e fevereiro), garantindo o rito da Lei Complementar nº 141/2012",
        "Monitorar mensalmente e quadrimestralmente as informações e identificar metas que estão abaixo do esperado da proporção esperada para o período, a área técnica responsável deverá apresentar um Plano de Ação corretivo (utilizando ferramentas como PDCA ou 5W2H) na reunião de avaliação da Secretaria"
    ],
    "6.2.6": [
        "Estabelecer reunião mensal na Sala de Situação para revisar indicadores críticos",
        "Programar os painéis da Sala de Situação para emitir status visuais e alertas diante de inconsistências epidemiológicas"
    ],
    "6.2.7": [
        "Definir níveis hierárquicos de acesso ao Painel (perfil do secretário, diretor, técnico, gerente de UBS)",
        "Capacitar o corpo gerencial para a leitura analítica de painéis (Business Intelligence)",
        "Desenvolver uma interface pública do Painel (\"Painel da Transparência em Saúde\")"
    ],
    "6.2.8": [
        "Remanejar/contratar pessoal para compor equipe de gestão de custo",
        "Designar responsável técnico pela gestão e qualificação das informações de custos em cada estabelecimento de saúde",
        "Treinar a equipe técnica em metodologias padronizadas para elaboração de estudos de avaliação econômica, gestão de custos e análise de evidências científicas para subsidiar a tomada de decisão",
        "Implantar Banco de Dados institucional em tecnologias em saúde e avaliações econômicas",
        "Implementar sistema informatizado para gestão, análise e visualização de dados em saúde"
    ],
    "6.2.9": [
        "Acompanhar mensalmente a transmisssão das remessas de dados ao Ministério da Saúde",
        "Acompanhar produção ambulatorial para analise técnica dos relatorio de produção",
        "Monitorar a completude da operacionalização das informações inseridas nos sistemas de informação vigente",
        "Capacitar continuamente as equipes assistenciais e administrativas sobre o preenchimento no sistema de informação e formulários oficiais"
    ],
    "6.2.10": [
        "Instituir Grupo Condutor da Rede de Atenção à Saúde",
        "Monitoramento da efetividade das linhas de cuidado prioritárias da Secretaria Municipal da Saúde (SEMSA), em conformidade com as diretrizes do Ministério da Saúde, visando à organização da Rede de Atenção à Saúde e à integralidade do cuidado"
    ],
    "6.2.11": [
        "Capacitar profissionais de saúde para o registro no sistema e-SUS APS",
        "Adequar protocolos de segurança da informação e proteção de dados do paciente no sistema",
        "Assegurar a interoperabilidade dos registros eletrônicos em saúde entre os níveis de atenção e a integração com a Rede Nacional de Dados em Saúde (RNDS)"
    ],
    "6.3.1": [
        "Definir os técnicos responsáveis pelo levantamento de dados nas unidades de saúde",
        "Enviar mensalmente as planilhas de custos com dados levantados",
        "Implantar o Sistema ApuraSUS por unidade",
        "Alimentar os dados no ApuraSUS (Coordenação de Custos)",
        "Gerar os relatórios e retroalimentação (Coordenação de Custos)",
        "Capacitar o Pessoal"
    ],
    "6.4.1": [
        "Definir etapas, prazos intermediários e responsabilidades claras para análise, encaminhamento, resposta e fechamento das manifestações",
        "Estabelecer fluxos formais com os setores da Secretaria de Saúde, com definição de prazos internos inferiores a 30 dias e responsabilização pelo retorno das demandas"
    ],
    "6.4.2": [
        "Otimizar o fluxo de tramitação das manifestações, priorizando a digitalização completa do processo, desde a abertura até a resposta ao cidadão, eliminando etapas burocráticas",
        "Conceder autonomia à equipe da Ouvidoria para responder diretamente às manifestações de baixa complexidade (como pedidos de informação) sem necessidade de tramitação externa"
    ],
    "6.5.1": [
        "Realizar capacitações continuadas com temas diversos",
        "Articular parcerias com Escolas Técnicas do SUS (ETSUS) e organizações sociais",
        "Elaborar material didático de apoio"
    ],
    "6.5.2": [
        "Planejar e executar as Ações e Atividades inerentes a conferência de Saúde",
        "Mobilizar a sociedade para a realização das pré-conferências e conferência de saúde",
        "Articular parcerias com o Conselho Estadual/Nacional de Saúde"
    ],
    "6.5.3": [
        "Contratar/desenvolver o portal do CMS",
        "Criar o canal oficial no YouTube",
        "Transmitir ao vivo as reuniões ordinárias do Conselho",
        "Publicar mensalmente as pautas, atas e resoluções no portal",
        "Parceria com ouvidoria sus",
        "Parceria ouvidoria municipal",
        "Visita técnica nos estabelecimentos de saúde",
        "Realizar palestras com a comunidade",
        "Realiza seminário temático"
    ],
    "7.1.1": [
        "Desenvolver ações de saúde ocupacional, prevenção e promoção à saúde do trabalhador",
        "Fortalecer os grupos terapêuticos, oficinas de autocuidado, rodas de conversa e atendimento em rede",
        "Promover campanhas e ações integradas de promoção à saúde e qualidade de vida no trabalho (alimentação, atividade física, ergonomia, prevenção ao adoecimento psíquico)",
        "Realizar ações descentralizadas nos locais de trabalho, com equipes itinerantes",
        "Incentivar hábitos saudáveis como a prática de atividade física e dieta equilibrada, e oferecer melhores condições para o desempenho das atividades laborais",
        "Ampliar o cuidado integral aos trabalhadores SEMSA, garantindo o acesso aos serviços de saúde para diagnóstico, tratamento e reabilitação física e mental",
        "Reduzir recorrência e absenteísmo por adoecimento do trabalhador da SEMSA",
        "Sistematizar o acompanhamento em processos de adoecimento (físico e mental)",
        "Implementar o acompanhamento dos trabalhadores em afastamento, readaptação e retorno ao trabalho",
        "Ambientar o servidor, juntamente com a coordenação de Humanização, nos casos de readaptação e retorno ao trabalho"
    ],
    "7.1.2": [
        "Elaborar Plano de Educação Permanente/SEMSA",
        "Implantar Centro de Capacitação de Educação Permanente da SEMSA",
        "Elaborar agenda integrada de educação permanente, no âmbito da SEMSA",
        "Monitorar a aplicabilidade da agenda integrada, no âmbito da SEMSA",
        "Realizar curso introdutório de novos servidores da SEMSA, em até 30 dias após sua admissão ou mudança de setor de trabalho",
        "Realizar curso de qualificação em gestão de serviços de saúde para, no mínimo 80% dos gerentes das UBS, até 2029"
    ],
    "7.1.3": [
        "Elaborar e instituir o Plano Municipal de Integração Ensino-Serviço até dezembro de 2028",
        "Implementar ações ao Plano Municipal de Integração Ensino-Serviço de acordo com as Diretrizes de integração ensino-serviço do SUS",
        "Formalizar a articulação entre universidades, escolas técnicas e a SEMSA para o desenvolvimento de atividades de ensino, estágios, residência e capacitação continuada, promovendo integração efetiva entre educação e serviço de saúde",
        "Georreferenciar as unidades de estágios, residências e afins, identificando as IES vinculadas, até 2028",
        "Promover ambientação para os preceptores dos campos de prática de estágios e residências multiprofissionais",
        "Implantar, até 2028, 01 sala (administrativa e técnica) da COREME e COREMU",
        "Fortalecer a gestão ensino-serviço por meio da articulação entre SEMSA e instituições de ensino"
    ],
    "7.1.5": [
        "Implementar Grupos de Trabalho de Humanização (GTHs) em, no mínimo, 60% dos serviços de saúde elegiveis da SEMSA",
        "Elaborar diagnóstico situacional das práticas de humanização no SUS nos estabelecimentos de saúde da SEMSA, identificando pontos fortes, fragilidades e oportunidades de melhoria, visando à qualificação do atendimento e fortalecimento da gestão centrada no usuário",
        "Realizar anualmente 1 Ação de boas práticas no SUS Parauapebas",
        "Realizar anualmente 1 Forúm Municipal de Humanização"
    ]
}

def format_action_list(actions):
    """Format a list of actions as a TypeScript array string."""
    if not actions:
        return None
    formatted = []
    for action in actions:
        escaped = action.replace('\\', '\\\\').replace('"', '\\"')
        formatted.append(f'        "{escaped}"')
    return '[\n' + ',\n'.join(formatted) + '\n    ]'

# Process the content - add actions to metas that don't have them
for meta_num, actions in ACTIONS.items():
    # Find the meta entry
    # Pattern: "num": "X.X.X", ... (with possible other fields between num and acoes or end of object)
    pattern = rf'("num":\s*"{re.escape(meta_num)}".*?)(\n\s*\}})'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        meta_section = match.group(1)
        end_brace = match.group(2)
        
        # Check if this meta already has acoes
        if '"acoes"' in meta_section:
            print(f"Meta {meta_num} já possui ações - pulando")
            continue
        
        # Format the new acoes
        acoes_str = format_action_list(actions)
        if acoes_str:
            # Insert acoes before the closing brace
            new_section = meta_section + ',\n    "acoes": ' + acoes_str + end_brace
            content = content[:match.start()] + new_section + content[match.end():]
            print(f"Meta {meta_num}: {len(actions)} ações adicionadas")
    else:
        print(f"AVISO: Meta {meta_num} não encontrada no arquivo")

# Write the updated content
with open(r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\src\lib\metas.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nArquivo metas.ts atualizado com sucesso!")
