Here's a possible patch that you can apply to the failing client code:

```java
@org.junit.jupiter.api.Test
void shouldPullPushedByDigest() throws java.lang.Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final java.lang.String output = this.client.run("pull", this.image.remoteByDigest());
    boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", this.image.remoteByDigest()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + this.image.remoteByDigest()));
    org.junit.jupiter.api.Assertions.assertFalse(contains);
}
```

The patch modifies the original code by introducing a new variable `contains` that stores the result of the `contains` method. The `assertThat` method is then called with the `output` and a new `StringContains` instance, which now only takes a single argument. Finally, the `assertFalse` method from JUnit Jupiter is used to check that the `contains` variable is false.