import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

class S {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for (int testCase = 0; testCase < tc; testCase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());

            int[][] grid = new int[n][m];
            Map<Integer, Integer> rowMax = new HashMap<>();
            Map<Integer, Integer> colMax = new HashMap<>();
            int safeCells = 0;

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < m; j++) {
                    grid[i][j] = Integer.parseInt(st.nextToken());
                    rowMax.put(i, Math.max(rowMax.getOrDefault(i, 0), grid[i][j]));
                    colMax.put(j, Math.max(colMax.getOrDefault(j, 0), grid[i][j]));
                }
            }

            for (int i = 0; i < q; i++) {
                st = new StringTokenizer(br.readLine());
                int r = Integer.parseInt(st.nextToken()) - 1;
                int c = Integer.parseInt(st.nextToken()) - 1;
                int x = Integer.parseInt(st.nextToken());

                grid[r][c] = x;
                rowMax.put(r, Math.max(rowMax.getOrDefault(r, 0), x));
                colMax.put(c, Math.max(colMax.getOrDefault(c, 0), x));
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (grid[i][j] == rowMax.get(i) || grid[i][j] == colMax.get(j)) {
                        safeCells++;
                    }
                }
            }

            System.out.println(safeCells);
        }

        br.close();
    }
}
