const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

async function main() {
  const sites = await prisma.site.findMany({
    orderBy: { updatedAt: 'desc' },
    take: 3
  });
  sites.forEach(s => {
    console.log(`\nSITE: ${s.name}`);
    console.log(`CONFIG: ${s.config}`);
  });
}

main().finally(() => prisma.$disconnect());
