const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

async function main() {
  const logs = await prisma.log.findMany({
    orderBy: { createdAt: 'desc' },
    take: 15
  });
  console.log("LAST 15 LOGS:");
  logs.forEach(l => console.log(`[${l.type}] ${l.message}`));
}

main().finally(() => prisma.$disconnect());
