
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class Solution  {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();

        for (int tc = 0; tc < t; tc++) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int q = scanner.nextInt();

            int[][] mold = new int[n][m];
            int[] rowMax = new int[n];
            Set<Integer> rowSet = new HashSet<>();

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    mold[i][j] = scanner.nextInt();
                }
                rowMax[i] = maxArray(mold[i]);
                rowSet.add(rowMax[i]);
            }

            int[] colMax = maxColumns(mold);
            Set<Integer> colSet = new HashSet<>();
            for (int max : colMax) {
                colSet.add(max);
            }

            int ans = 0;

            for (int i = 0; i < q; i++) {
                int r = scanner.nextInt();
                int c = scanner.nextInt();
                int x = scanner.nextInt();

                mold[r - 1][c - 1] = x;

                if (rowMax[r - 1] < x) {
                    rowSet.remove(rowMax[r - 1]);
                    rowMax[r - 1] = x;
                    rowSet.add(x);
                }

                if (colMax[c - 1] < x) {
                    colSet.remove(colMax[c - 1]);
                    colMax[c - 1] = x;
                    colSet.add(x);
                }

                ans += countCommonValues(rowSet, colSet);
            }

            System.out.println("#" + (tc + 1) + " " + ans);
        }

        scanner.close();
    }

    // 배열의 최대값을 반환하는 메소드
    public static int maxArray(int[] arr) {
        int max = arr[0];
        for (int num : arr) {
            max = Math.max(max, num);
        }
        return max;
    }

    // 열의 최대값 배열을 반환하는 메소드
    public static int[] maxColumns(int[][] arr) {
        int n = arr.length;
        int m = arr[0].length;
        int[] maxArr = new int[m];

        for (int j = 0; j < m; j++) {
            int max = arr[0][j];
            for (int i = 1; i < n; i++) {
                max = Math.max(max, arr[i][j]);
            }
            maxArr[j] = max;
        }

        return maxArr;
    }

    // 두 개의 Set에 공통된 값을 카운트하는 메소드
    public static int countCommonValues(Set<Integer> set1, Set<Integer> set2) {
        int count = 0;
        for (int num : set1) {
            if (set2.contains(num)) {
                count++;
            }
        }
        return count;
    }
}
