Here is a patch that you can apply to the failing method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime());
}

private Timestamp adaptDateToTimestamp(Date date) {
    return new Timestamp(date.getTime());
}

@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return adaptDateToTimestamp(super.between(adaptDateToTimestamp(from), adaptDateToTimestamp(to)));
}
```

This patch introduces a new private method `adaptDateToTimestamp` which converts a `Date` object to a `Timestamp` object. This allows the `between` method to use the new `Timestamp`-based implementation in the superclass, while still returning a `Timestamp` object as required.

Note that this patch retains the original method signature and does not use any removed library methods. It does, however, use the added `Timestamp`-based `between` method in the superclass.