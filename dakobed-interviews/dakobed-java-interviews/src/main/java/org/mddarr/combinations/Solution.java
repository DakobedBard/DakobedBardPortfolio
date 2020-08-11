package org.mddarr.combinations;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target){
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        findCombinations(candidates, 0, target, new ArrayList<Integer>(), result);
        return result;
    }
    private void findCombinations(int[] candidates, int index, int target,List<Integer> current,  List<List<Integer>> result){
        if(target == 0){
            result.add(current);
            return;
        }
        if(target<0)
            return;
        for(int i = index; i< candidates.length; i++){
            current.add(candidates[i]);
            findCombinations(candidates, index+1, target-candidates[i], current, result);

        }
    }


}
