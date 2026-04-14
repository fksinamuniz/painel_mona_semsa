"use server";

import { prisma } from "@/lib/prisma";
import bcrypt from "bcryptjs";

export async function adminSetup(formData: FormData) {
    const username = formData.get("username") as string;
    const password = formData.get("password") as string;

    if (!username || !password) throw new Error("Preencha todos os campos");

    // Check if any user exists
    const userCount = await prisma.user.count();
    if (userCount > 0) throw new Error("O administrador já foi cadastrado");

    const hashedPassword = await bcrypt.hash(password, 10);

    const user = await prisma.user.create({
        data: {
            username,
            password: hashedPassword,
        },
    });

    return { success: true };
}

export async function login(formData: FormData) {
    return { success: true };
}

export async function logout() {
    return { success: true };
}

export async function checkAdminExists() {
    const count = await prisma.user.count();
    return count > 0;
}
