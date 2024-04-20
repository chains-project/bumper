Here's the proposed patch for the failing method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(new Timestamp(from.getTime()), new Timestamp(to.getTime())).getTime());
}
```

This patch converts the `Date` arguments to `Timestamp` before passing them to the superclass method, since the new library version only provides a `between` method that takes `Timestamp` arguments.