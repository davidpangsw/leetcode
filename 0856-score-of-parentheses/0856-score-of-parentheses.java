class Solution {
    private int p = 0;
    public int scoreOfParentheses(String s) {
        int score = 0;
        while (p < s.length()) {
            score += helper(s);
        }
        return score;
    }

    // score
    public int helper(String s) {
        // s[p] must be '('
        p++;

        if (s.charAt(p) == ')') {
            p++;
            return 1;
        }

        int score = 0;
        while (s.charAt(p) == '(') {
            score += helper(s);
        }

        // s[p] must be ')'
        p++;
        return score * 2;
    }
}