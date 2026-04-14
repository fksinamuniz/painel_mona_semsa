import { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";

export const authOptions: NextAuthOptions = {
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: {
        username: { label: "Username", type: "text", placeholder: "admin" },
        password: { label: "Password", type: "password", placeholder: "admin" }
      },
      async authorize(credentials) {
        // Acesso para o usuário fksina
        if (credentials?.username === "fksina" && credentials?.password === "12345678") {
          return { id: "2", name: "FK Sina", email: "fksina@painel.digisus" }
        }
        // Simulando um login padrão (admin/admin) para atender à demanda de apenas login com armazenamento local
        if (credentials?.username === "admin" && credentials?.password === "admin") {
          return { id: "1", name: "Admin", email: "admin@painel.digisus" }
        }
        return null;
      }
    })
  ],
  pages: {
    signIn: "/login",
  },
  session: {
    strategy: "jwt"
  },
  secret: process.env.NEXTAUTH_SECRET || "minha_chave_super_secreta_pra_desenvolvimento",
};
