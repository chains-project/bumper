Here's a possible patch for the given code snippet:

```java
  @Override
  public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    long fromTime = from.getTime();
    long toTime = to.getTime();
    return new Timestamp(super.between(from, to).getTime());
  }
```
This patch creates two new variables `fromTime` and `toTime` to store the time in milliseconds of the `from` and `to` dates, respectively. This allows the `Timestamp` constructor to be called with a `long` argument, which is the expected type.