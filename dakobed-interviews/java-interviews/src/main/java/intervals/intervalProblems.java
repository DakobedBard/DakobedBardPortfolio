package intervals;

public class intervalProblems {
    public static void main(String[] args) {
        int[][] intervals = {
                {1,3},{2,6}, {8,10}, {15,18}
        };
        Solution solution = new Solution();
        int[][] mergedIntervals = solution.merge(intervals);
        for(int[] interval: mergedIntervals){
            System.out.println(interval[0] + " " + interval[1]);
        }
    }
}
