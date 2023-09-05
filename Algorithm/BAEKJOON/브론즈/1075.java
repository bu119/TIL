import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // 입력 데이터 읽기

        String str = reader.readLine();  // Hi Anna
        System.out.println(str);

        // 입력 데이터 출력
        // System.out.println(str);  // Hi Anna
//        String[] str = reader.readLine().split(" ");
    }
}