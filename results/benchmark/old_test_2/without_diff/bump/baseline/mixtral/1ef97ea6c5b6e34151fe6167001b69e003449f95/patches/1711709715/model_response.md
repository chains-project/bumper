Sure, I can help you with that. Here is a fixed version of your `between` method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    long time = super.between(from, to).getTime();
    return new Timestamp(time);
}
```

In this version, we first extract the time in milliseconds from the `Date` object returned by the superclass method, and then use that value to create a new `Timestamp` object. This avoids the incompatible types error you were seeing.