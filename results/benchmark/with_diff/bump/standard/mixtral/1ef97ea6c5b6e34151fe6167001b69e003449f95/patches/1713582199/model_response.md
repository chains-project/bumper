Here is a patch that you can apply to the `between` method in the `DateTime` class:
```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(new Timestamp(from.getTime()), new Timestamp(to.getTime())).getTime());
}
```
This patch converts the `Date` objects to `Timestamp` objects before passing them to the `between` method of the superclass. This is necessary because the superclass's `between` method now expects `Timestamp` objects as its arguments, rather than `Date` objects.

I hope this helps! Let me know if you have any questions.