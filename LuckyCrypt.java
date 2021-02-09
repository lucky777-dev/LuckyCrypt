/*
LuckyCrypt
Version : 1.0
Author : LuckySmile :)
2021
*/

public class LuckyCrypt {
    public static void main(String[] args) {
        util.clearScreen();
        /* util.slowPrint("LuckyCrypt v1.0");
        util.slowPrint("\nby LuckySmile :)"); */
        util.clearScreen();
        int choice = menu();
        while (choice != 0) {
            switch (choice) {
                case 1:
                    modules.choice1();
                    util.clearScreen();
                    break;
                case 2:
                    modules.choice2();
                    util.clearScreen();
                    break;
                case 3:
                    modules.choice3();
                    util.clearScreen();
                    break;
                case 4:
                    modules.choice4();
                    util.clearScreen();
                    break;
            }
            choice = menu();
        }
        util.clearScreen();
        System.out.println("LuckyCrypt v1.0");
        System.out.println("by LuckySmile :)\n");
        util.slowPrint("See you :) !");
        System.out.println();
        util.clearScreen();
    }

    public static int menu() {
        System.out.println("LuckyCrypt v1.0");
        System.out.println("by LuckySmile :)\n");
        util.fastPrint("1. Encrypt\n");
        util.fastPrint("2. Decrypt\n");
        util.fastPrint("3. Encrypt file\n");
        util.fastPrint("4. Decrypt file\n");
        util.fastPrint("0. Quit\n\n");
        int choice = util.askIntRange("Make your choice", 0, 4);
        return choice;
    }
}
