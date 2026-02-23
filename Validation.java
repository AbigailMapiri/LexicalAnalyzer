import java.util.Scanner;
import java.util.regex.Pattern;

public class Validation {

    // Compile patterns once (better performance)
    private static final Pattern DATE_PATTERN = Pattern.compile(
            "^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$");

    private static final Pattern URL_PATTERN = Pattern.compile(
            "^(https://)?(www\\.)[a-zA-Z]+\\.bw$");

    private static final Pattern EMAIL_PATTERN = Pattern.compile(
            "^[a-zA-Z]+(\\.[a-zA-Z]+)?@[a-zA-Z]+\\.bw$");

    // Enum for validation types
    enum ValidationType {
        DATE, URL, EMAIL
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("==== VALIDATION SYSTEM ====");

        while (true) {
            System.out.println("\nChoose validation type:");
            System.out.println("1. Date (dd/mm/yyyy)");
            System.out.println("2. URL (.bw)");
            System.out.println("3. Email (.bw)");
            System.out.println("4. Exit");

            int choice = scanner.nextInt();
            scanner.nextLine(); // consume newline

            if (choice == 4) {
                System.out.println("Exiting program...");
                break;
            }

            System.out.print("Enter value to validate: ");
            String input = scanner.nextLine();

            boolean result = false;

            switch (choice) {
                case 1:
                    result = validate(ValidationType.DATE, input);
                    break;
                case 2:
                    result = validate(ValidationType.URL, input);
                    break;
                case 3:
                    result = validate(ValidationType.EMAIL, input);
                    break;
                default:
                    System.out.println("Invalid option.");
                    continue;
            }

            System.out.println("Validation Result: " + result);
        }

        scanner.close();
    }

    // Improved validation method
    public static boolean validate(ValidationType type, String input) {

        switch (type) {
            case DATE:
                return DATE_PATTERN.matcher(input).matches();
            case URL:
                return URL_PATTERN.matcher(input).matches();
            case EMAIL:
                return EMAIL_PATTERN.matcher(input).matches();
            default:
                return false;
        }
    }
}