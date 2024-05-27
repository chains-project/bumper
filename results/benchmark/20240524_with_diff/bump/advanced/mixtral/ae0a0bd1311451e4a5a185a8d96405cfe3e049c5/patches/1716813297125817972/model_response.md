Here is a potential patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldPullPushedByTag() throws java.lang.Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final java.lang.String output = this.client.run("pull", this.image.remote());
    boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", this.image.remote()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + this.image.remote()));
}
```
Explanation:

The error message indicates that the constructor for `StringContains` is expecting a single `String` argument, but is receiving a `boolean` and a `String`. This suggests that the `StringContains` constructor has changed in the new library version, and no longer accepts a `boolean` argument.

To fix the error, we can replace the use of the `StringContains` constructor with a `contains` method call on the `output` string. This will check if the `output` string contains the specified substring, and return a `boolean` value indicating the result. We can then pass the result of this call to the `StringContains` constructor.

Additionally, we need to update the argument passed to the `StringContains` constructor to match the updated constructor signature. Instead of passing a `boolean` value, we can pass a `String` value that includes the substring we want to check for.

With these changes, the client code should be able to compile and run successfully with the new library version.