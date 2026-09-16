function hello(): void {
    console.log("Hello");
    }

function error(message: string): never {
    throw new Error(message);
    }
