const solution = (arr1, arr2) => {
    return arr1.map((row) =>
        arr2[0].map((_, cIdx) =>
            row.reduce((acc, cur, rIdx) =>
                acc + cur * arr2[rIdx][cIdx]
            , 0)
        )
    );
}
