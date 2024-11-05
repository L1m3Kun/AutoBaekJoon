const solution = (absolutes, signs) => absolutes.reduce((prev, now, i) => prev + now * (signs[i] ? 1 : -1), 0);
