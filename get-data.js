const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

async function main() {
  const extractions = await prisma.extraction.findMany({
    orderBy: { createdAt: 'desc' },
    take: 3,
    include: { site: true }
  });
  extractions.forEach(e => {
    console.log(`\nSITE: ${e.site.name} | INSTRUCTIONS: ${e.site.instructions}`);
    console.log(`DATA: ${e.data}`);
  });
}

main().finally(() => prisma.$disconnect());
