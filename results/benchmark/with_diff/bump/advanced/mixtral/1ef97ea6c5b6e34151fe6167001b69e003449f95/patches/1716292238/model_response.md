Here's a patch that you can apply to the `between` method in order to fix the error:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(new Timestamp(from.getTime()), new Timestamp(to.getTime())).getTime());
}
```

This patch converts the `Date` objects to `Timestamp` objects before passing them to the `super.between` method, since the new library version expects `Timestamp` arguments.