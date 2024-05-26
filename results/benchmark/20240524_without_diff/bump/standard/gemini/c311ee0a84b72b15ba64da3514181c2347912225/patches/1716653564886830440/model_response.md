```java
// Add a static import for the StringContains matcher.
import static org.hamcrest.CoreMatchers.stringContainsInOrder;

// Update the assertion to use the StringContainsInOrder matcher.
org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", Throwables.getRootCause(throwable).getMessage(), stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
```