import java.util.*;
import java.util.ArrayList;
import java.io.*;

public class LexicalAnalyzer {

    // Java keywords
    static Set<String> keywords = new HashSet<>(Arrays.asList ("int", "float", "double", "if", "else", "while", "for", "return", "public", "class", "static", "void"));

    // Operators
    static Set<Character> operators = new HashSet<>(Arrays.asList('+', '-', '*', '/', '=', '<', '>', '!'));

    // Separators
    static Set<Character> separators = new HashSet<>(Arrays.asList(  ';', ',', '(', ')', '{', '}'));

    public static void main(String[] args) {

        String input = "int number = 10;";

        int i = 0;

        while (i < input.length()) {

            char ch = input.charAt(i);

            // Ignore whitespace
            if (Character.isWhitespace(ch)) {
                i++;
                continue;
            }

            // IDENTIFIER or KEYWORD
            if (Character.isLetter(ch)) {
                StringBuilder sb = new StringBuilder();

                while (i < input.length() &&
                        (Character.isLetterOrDigit(input.charAt(i)))) {

                    sb.append(input.charAt(i));
                    i++;
                }

                String word = sb.toString();

                if (keywords.contains(word)) {
                    System.out.println(word + " -> KEYWORD");
                } else {
                    System.out.println(word + " -> IDENTIFIER");
                }
            }

            // NUMBER
            else if (Character.isDigit(ch)) {
                StringBuilder sb = new StringBuilder();

                while (i < input.length() &&
                        Character.isDigit(input.charAt(i))) {

                    sb.append(input.charAt(i));
                    i++;
                }

                System.out.println(sb.toString() + " -> NUMBER");
            }

            // OPERATOR
            else if (operators.contains(ch)) {
                System.out.println(ch + " -> OPERATOR");
                i++;
            }

            // SEPARATOR
            else if (separators.contains(ch)) {
                System.out.println(ch + " -> PUNCTUATION");
                i++;
            }

            else {
                System.out.println(ch + " -> UNKNOWN");
                i++;
            }
        }
    }
}
