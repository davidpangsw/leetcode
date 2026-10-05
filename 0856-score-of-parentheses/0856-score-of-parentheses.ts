
function scoreOfParentheses(s: string): number {
    let scores = [0]
    for (const c of s) {
        if (c == '(') {
            scores.push(0);
        } else {
            const last = scores.pop();
            if (last == 0) {
                scores[scores.length - 1] += 1;
            } else {
                scores[scores.length - 1] += last * 2;
            }
        }
    }
    return scores.pop();
};