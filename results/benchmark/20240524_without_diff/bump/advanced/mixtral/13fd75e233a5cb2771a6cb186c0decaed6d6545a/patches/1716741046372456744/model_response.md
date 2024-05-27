Here is a fixed version of the code:
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
The issue was caused by the incorrect usage of the `StringContains` constructor. It expects a single `String` argument, but it received a `boolean` and a `String`. I have modified the code to first check if the output string contains the expected substring using the `contains` method of the `String` class, and then use the `StringContains` constructor with the expected substring.