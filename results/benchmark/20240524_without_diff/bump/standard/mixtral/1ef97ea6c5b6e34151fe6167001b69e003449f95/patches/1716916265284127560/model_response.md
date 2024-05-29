Here's the fixed version of the `between` method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime());
}
```

The code you provided is actually correct, but the error message you received may be caused by the return type of the method that calls `between`. You should check the method that calls `DateTime.between` and make sure it can handle the `Timestamp` return type.

If you are sure that the calling method can handle `Timestamp`, then the error may be caused by an incompatible version of the `Date` or `Timestamp` class. You can try updating your project dependencies to the latest version to see if it resolves the issue.