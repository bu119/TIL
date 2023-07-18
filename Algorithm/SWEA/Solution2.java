import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());

        for (int tc = 0; tc < t; tc++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());

            int[][] mold = new int[n][m];
            int[] rowMax = new int[n];
            int[] colMax = new int[m];

            Set<Integer> rowSet = new HashSet<>();

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < m; j++) {
                    mold[i][j] = Integer.parseInt(st.nextToken());
                    rowMax[i] = Math.max(rowMax[i], mold[i][j]);
                    colMax[j] = Math.max(colMax[j], mold[i][j]);
                }
                rowSet.add(rowMax[i]);
            }

            int ans = 0;

            int maxRow = Arrays.stream(rowMax).max().orElse(0);
            int maxCol = Arrays.stream(colMax).max().orElse(0);


            for (int i = 0; i < q; i++) {
                st = new StringTokenizer(br.readLine());
                int r = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());

                mold[r - 1][c - 1] = x;

                if (rowMax[r - 1] < x) {
                    rowSet.remove(rowMax[r - 1]);
                    rowMax[r - 1] = x;
                    rowSet.add(x);
                }

                if (colMax[c - 1] < x) {
                    colMax[c - 1] = x;
                }

                ans += countCommon(rowSet, colMax);
            }

            System.out.println("#" + (tc + 1) + " " + ans);
        }

        br.close();
    }

    static int countCommon(Set<Integer> set1, int[] int2, int maxRow, int maxCol) {
        int count = 0;
        Set<Integer> int2Set = new HashSet<>();
        for (int value : int2) {
            int2Set.add(value);
        }

        // 집합의 교집합 계산
        Set<Integer> commonSet = new HashSet<>(set1);
        commonSet.retainAll(int2Set);

        for (int value : commonSet) {
            if (value <= maxRow && value <= maxCol) {
                count++;
            }
        }
        return count;
    }
}