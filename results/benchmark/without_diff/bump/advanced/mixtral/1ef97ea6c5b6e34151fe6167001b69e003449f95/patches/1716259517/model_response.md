Here's the fixed version of the `between` method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime());
}
```

The code you provided is actually correct, but the error message you received suggests that the issue might be caused by the types of the `from` and `to` parameters.

To fix the issue, you can ensure that the `from` and `to` parameters are of type `java.sql.Date` instead of `java.util.Date`. This can be done by changing the type of the parameters in the method signature or by converting the `from` and `to` parameters to `java.sql.Date` using the appropriate constructor before passing them to the `super.between()` method.

Here's an updated version of the method that converts the `from` and `to` parameters to `java.sql.Date`:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(new java.sql.Date(from.getTime()), new java.sql.Date(to.getTime())).getTime());
}
```

This should fix the incompatible types error you were seeing.