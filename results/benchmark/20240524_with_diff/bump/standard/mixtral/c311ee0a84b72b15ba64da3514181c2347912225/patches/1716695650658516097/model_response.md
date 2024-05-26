Here's a possible patch for the code to fix the error:
```java
@org.junit.jupiter.api.Test
void shouldPullPushedByDigest() throws java.lang.Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final java.lang.String output = this.client.run("pull", this.image.remoteByDigest());
    boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", this.image.remoteByDigest()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + this.image.remoteByDigest()));
}
```
The error message indicates that the constructor for `StringContains` now requires a single string argument, rather than a boolean and a string. To fix this, I replaced the boolean expression `false` with a call to the `contains` method on the `output` string. Additionally, I updated the `assertThat` statement to use the new constructor for `StringContains`.