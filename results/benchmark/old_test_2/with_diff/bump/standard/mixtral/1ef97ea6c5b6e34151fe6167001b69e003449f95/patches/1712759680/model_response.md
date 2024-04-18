Here is the proposed patch for the failing method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).toInstant().toEpochMilli());
}
```
In this patch, I changed the `super.between(from, to)` to use the new method in the library, which returns a `Timestamp` instead of a `Date`. I also changed the `getTime()` method to `toInstant().toEpochMilli()` to convert the `Timestamp` to a number of milliseconds since January 1, 1970, 00:00:00.000 GMT, which is the same as the `getTime()` method in the `Date` class.