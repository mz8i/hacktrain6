/**
 * Memoize the results of a function.
 * Works only with functions whose parameters are easily serializable to string
 * @param fn 
 */
export function withMemoize(fn: Function) {
    const cache = {};

    return (...args) => {
        const cacheKey = args.map(x => x+'').join('@@');

        if(!cache.hasOwnProperty(cacheKey)) {
            console.log('First time computing fn for '+cacheKey);
            cache[cacheKey] = fn(...args);
        }

        return cache[cacheKey];
    };
}
