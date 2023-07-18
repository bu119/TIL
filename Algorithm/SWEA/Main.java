import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int tc = 0; tc < t; tc++) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int q = scanner.nextInt();
            int[][] mold = new int[n][m];

            int ans = 0;
            int[] rowMax = new int[n];
            int[] colMax = new int[m];

            PriorityQueue<Cell> cells = new PriorityQueue<>((a, b) -> b.value - a.value);


            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    mold[i][j] = scanner.nextInt();
                    rowMax[i] = Math.max(rowMax[i], mold[i][j]);
                    colMax[j] = Math.max(colMax[j], mold[i][j]);
                    cells.offer(new Cell(i, j, mold[i][j]));
                }
            }


            for (int k = 0; k < q; k++) {
                int r = scanner.nextInt() - 1;
                int c = scanner.nextInt() - 1;
                int x = scanner.nextInt();

                rowMax[r] = Math.max(rowMax[r], x);
                colMax[c] = Math.max(colMax[c], x);
                cells.offer(new Cell(r, c, x));

                while (!cells.isEmpty()) {
                    Cell cell = cells.peek();
                    if (cell.value != mold[cell.row][cell.col]) {
                        cells.poll();
                    } else {
                        break;
                    }
                }

                if (cells.isEmpty()) {
                    ans = 0;
                } else {
                    Cell cell = cells.peek();
                    if (cell.value == rowMax[cell.row] && cell.value == colMax[cell.col]) {
                        ans = cells.size();
                    } else {
                        ans = cells.size() - 1;
                    }
                }

            }
            System.out.println("#" + (tc + 1) + " " + ans);
        }

        scanner.close();
    }
}

class Cell {
    int row;
    int col;
    int value;

    public Cell(int row, int col, int value) {
        this.row = row;
        this.col = col;
        this.value = value;
    }
}
