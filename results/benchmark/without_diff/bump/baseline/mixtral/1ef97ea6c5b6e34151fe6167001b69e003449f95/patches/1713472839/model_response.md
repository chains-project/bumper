Here's a possible patch for the given code:

```java
  @Override
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    long time = super.between(from, to).getTime();
    return new Timestamp(time);
  }
```

In this patch, I created a new variable `time` to store the time in milliseconds returned by the `getTime()` method of the `Date` object returned by the superclass's `between()` method. Then, I used the `Timestamp` constructor that takes a long argument representing the number of milliseconds since January 1, 1970, 00:00:00.000 GMT. This constructor returns a `Timestamp` object, which is compatible with the method's return type.