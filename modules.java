
import java.util.Scanner;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class modules {

    static Scanner kb = new Scanner(System.in);

    public static void choice1() {
        util.clearScreen();
        System.out.println("LuckyCrypt v1.0");
        System.out.println("by LuckySmile :)\n");
        util.slowPrint("< Encrypt >");
        System.out.println("\n");
        String msg = util.askValidMsg("encrypt");
        String key = util.askValidKey();
        String encrypted = encrypt(msg, key);
        util.fastPrint("\nOriginal  : ");
        util.sleep(1);
        util.fastPrint(msg);
        util.sleep(1);
        util.fastPrint("\nEncrypted : ");
        util.sleep(1);
        util.fastPrint(encrypted);
        util.sleep(1);
        System.out.println("\n");
        if (util.askYN("Do you want to save it in [Save.txt] ?")) {
            saveMsg("ENCRYPTED", msg, encrypted);
            util.fastPrint("\nYour data has been saved in [Save.txt]\n\n");
            util.enter();
        }
    }

    public static void choice2() {
        util.clearScreen();
        System.out.println("LuckyCrypt v1.0");
        System.out.println("by LuckySmile :)\n");
        util.slowPrint("< Decrypt >");
        System.out.println("\n");
        String msg = util.askValidMsg("decrypt");
        String key = util.askValidKey();
        String decrypted = decrypt(msg, key);
        util.fastPrint("\nEncrypted : ");
        util.sleep(1);
        util.fastPrint(msg);
        util.sleep(1);
        util.fastPrint("\nDecrypted : ");
        util.sleep(1);
        util.fastPrint(decrypted);
        util.sleep(1);
        System.out.println("\n");
        if (util.askYN("Do you want to save it in [Save.txt] ?")) {
            saveMsg("DECRYPTED", msg, decrypted);
            util.fastPrint("\nYour data has been saved in [Save.txt]\n\n");
            util.enter();
        }

    }

    public static void choice3() {
        util.clearScreen();
        System.out.println("LuckyCrypt v1.0");
        System.out.println("by LuckySmile :)\n");
        String filesList[] = util.getFiles();
        if (filesList[0].equals("<error> No txt files found")) {
            util.fastPrint("! <error> No files detected...");
            util.sleep(1);
            util.fastPrint("\n\nPlease copy the file yout want to encrypt in the same directory as [LuckyCrypt.jar]");
            util.fastPrint("\n\n(Make sure this is a [.txt] file)\n\n");
            util.enter();
        } else {
            util.slowPrint("< Encrypt File >");
            System.out.println("\n");
            for (int i = 0; i < filesList.length; i++) {
                if (i < 10) {
                    util.fastPrint(" " + (i + 1) + " : " + filesList[i] + "\n");
                } else {
                    util.fastPrint((i + 1) + " : " + filesList[i] + "\n");
                }
            }
            util.fastPrint(" 0 : exit\n");
            util.fastPrint("\n" + filesList.length + " file(s) loaded !\n\n");
            String path = util.askValidFileName("encrypt", filesList);
            if (!path.equals("0.txt") && !path.equals("exit.txt") && !path.equals("quit.txt")) {
                String key = util.askValidKey();
                int nbLines = util.fileLineCounter(path);
                String[] text = new String[nbLines];
                String[] encrypted = new String[nbLines];
                text = util.readFile(path, text, nbLines);
                for (int i = 0; i < text.length; i++) {
                    encrypted[i] = encrypt(text[i], key);
                }
                util.fastPrint("\nOriginal : ");
                util.sleep(1);
                System.out.println();
                for (int i = 0; i < text.length; i++) {
                    util.fastPrint(text[i]);
                    if (i < text.length - 1) {
                        System.out.println();
                    }
                }
                util.sleep(1);
                util.fastPrint("\n\nEncrypted : ");
                util.sleep(1);
                System.out.println();
                for (int i = 0; i < encrypted.length; i++) {
                    util.fastPrint(encrypted[i]);
                    if (i < encrypted.length - 1) {
                        System.out.println();
                    }
                }
                util.sleep(1);

                System.out.println("\n");
                System.out.println();
                if (util.askYN(
                        "Do you want to save it in [" + path.substring(0, (path.length() - 4)) + "-encrypted.txt] ?")) {
                    String newPath = util.saveFile("ENCRYPTED", path, encrypted);
                    util.fastPrint("\nYour data has been saved in [" + newPath + "]\n\n");
                    util.enter();
                }
            }
        }
    }

    public static void choice4() {
        util.clearScreen();
        System.out.println("LuckyCrypt v1.0");
        System.out.println("by LuckySmile :)\n");
        String filesList[] = util.getFiles();
        if (filesList[0].equals("<error> No txt files found")) {
            util.fastPrint("! <error> No files detected...");
            util.sleep(1);
            util.fastPrint("\n\nPlease copy the file yout want to decrypt in the same directory as [LuckyCrypt.jar]");
            util.fastPrint("\n\nMake sure this is a [.txt] file\n\n");
            util.enter();
        } else {
            util.slowPrint("< Decrypt File >");
            System.out.println("\n");
            for (int i = 0; i < filesList.length; i++) {
                if (i < 10) {
                    util.fastPrint(" " + (i + 1) + " : " + filesList[i] + "\n");
                } else {
                    util.fastPrint((i + 1) + " : " + filesList[i] + "\n");
                }
            }
            util.fastPrint(" 0 : exit\n");
            util.fastPrint("\n" + filesList.length + " file(s) loaded !\n\n");
            String path = util.askValidFileName("decrypt", filesList);
            if (!path.equals("0.txt") && !path.equals("exit.txt") && !path.equals("quit.txt")) {
                String key = util.askValidKey();
                int nbLines = util.fileLineCounter(path);
                String[] text = new String[nbLines];
                String[] decrypted = new String[nbLines];
                text = util.readFile(path, text, nbLines);
                for (int i = 0; i < text.length; i++) {
                    decrypted[i] = decrypt(text[i], key);
                }
                util.fastPrint("\nEncrypted : ");
                util.sleep(1);
                System.out.println();
                for (int i = 0; i < text.length; i++) {
                    util.fastPrint(text[i]);
                    if (i < text.length - 1) {
                        System.out.println();
                    }
                }
                util.sleep(1);
                util.fastPrint("\n\nDecrypted : ");
                util.sleep(1);
                System.out.println();
                for (int i = 0; i < decrypted.length; i++) {
                    util.fastPrint(decrypted[i]);
                    if (i < decrypted.length - 1) {
                        System.out.println();
                    }
                }
                util.sleep(1);
                System.out.println("\n");
                if (util.askYN(
                        "Do you want to save it in [" + path.substring(0, (path.length() - 4)) + "-decrypted.txt] ?")) {
                    String newPath = util.saveFile("DECRYPTED", path, decrypted);
                    util.fastPrint("\nYour data has been saved in [" + newPath + "]\n\n");
                    util.enter();
                }
            }
        }
    }

    public static String encrypt(String msg, String key) {
        key = key.toLowerCase();
        int letterChar;
        for(int i=0; i<key.length(); i++) {
            if((int) key.charAt(i) < 97) {
                letterChar = (int) key.charAt(i) + 65;
                while(letterChar > 122) {
                    letterChar -= 26;
                }
                key = key.replace(key.charAt(i), (char) letterChar);
            }
            else if((int) key.charAt(i) > 122) {
                letterChar = (int) key.charAt(i) - 65;
                while(letterChar < 97) {
                    letterChar += 26;
                }
                key = key.replace(key.charAt(i), (char) letterChar);
            }
        }
        String encrypted = "";
        int charAscii;
        int cpt = 0;
        for (int i = 0; i < msg.length(); i++) {
            if ((int) msg.charAt(i) >= 32 && (int) msg.charAt(i) <= 126) {
                charAscii = (int) msg.charAt(i) + (int) key.charAt(cpt) - 96;
                if (charAscii > 126) {
                    charAscii -= 95;
                }
            } else {
                charAscii = (int) msg.charAt(i);
            }
            encrypted += (char) charAscii;
            cpt++;
            if (cpt == key.length()) {
                cpt = 0;
            }
        }
        return encrypted;
    }

    public static String decrypt(String msg, String key) {
        key = key.toLowerCase();
        int letterChar;
        for(int i=0; i<key.length(); i++) {
            if((int) key.charAt(i) < 97) {
                letterChar = (int) key.charAt(i) + 65;
                while(letterChar > 122) {
                    letterChar -= 26;
                }
                key = key.replace(key.charAt(i), (char) letterChar);
            }
            else if((int) key.charAt(i) > 122) {
                letterChar = (int) key.charAt(i) - 65;
                while(letterChar < 97) {
                    letterChar += 26;
                }
                key = key.replace(key.charAt(i), (char) letterChar);
            }
        }
        String decrypted = "";
        int charAscii;
        int cpt = 0;
        for (int i = 0; i < msg.length(); i++) {
            if ((int) msg.charAt(i) >= 32 && (int) msg.charAt(i) <= 126) {
                charAscii = (int) msg.charAt(i) - (int) key.charAt(cpt) + 96;
                if (charAscii < 32) {
                    charAscii += 95;
                }
            } else {
                charAscii = (int) msg.charAt(i);
            }
            decrypted += (char) charAscii;
            cpt++;
            if (cpt == key.length()) {
                cpt = 0;
            }
        }
        return decrypted;
    }

    public static void saveMsg(String mode, String msg, String result) {
        String first;
        String second;
        if (mode.equals("ENCRYPTED")) {
            first = "Original  : ";
            second = "Encrypted  : ";
        } else {
            first = "Encrypted : ";
            second = "Decrypted : ";
        }
        try {
            File file = new File("Save.txt");
            file.createNewFile();
        } catch (IOException ex) {
            System.out.println("\n\n! <error> Couldn't open file [Save.txt]");
        }
        try {
            FileWriter file = new FileWriter("Save.txt");
            file.write(first + msg + "\n" + second + result);
            file.close();
        } catch (IOException e) {
            System.out.println("\n\n! <error> Couldn't write in file [Save.txt]");
            e.printStackTrace();
        }
    }
}
