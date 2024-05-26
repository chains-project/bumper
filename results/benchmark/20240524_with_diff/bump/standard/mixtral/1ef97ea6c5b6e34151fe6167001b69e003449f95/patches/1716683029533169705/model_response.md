Here's a patch that you can apply to the failing method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime());
}

private Timestamp between(Date from, Date to) {
    return new Timestamp(super.between(from, to).getTime());
}

@Override
public Timestamp between(Timestamp from, Timestamp to) throws IllegalArgumentException {
    return between(from, to);
}
```

In the patched code, I added a new private method `between(Date from, Date to)` that converts the return value of `super.between(from, to)` to a `Timestamp`. Then, I overrode the method `between(Timestamp from, Timestamp to)` and made it call the new private method.

This way, the original method signature remains unchanged, and the error is handled within the client code.