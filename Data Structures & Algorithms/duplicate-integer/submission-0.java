

class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        HashMap<Integer, Integer> mapp = new HashMap<>();

        for (int i : nums){
            if (mapp.containsKey(i)){
                return true;
            }
            else{
                mapp.put(i, 0);
            }
        }

        return false;

    }
}