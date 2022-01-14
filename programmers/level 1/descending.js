function descending(n) {
    var answer = "";
    let stringn = String(n);
    let arr = []
    for (var i = 0; i < stringn.length; i++) {
        arr[i] = Number(stringn.charAt(i))
    }
    console.log(arr);
    arr.sort(function(a, b)  {
      return b - a;
    });
    answer = arr.join('');
    return Number(answer);
}
