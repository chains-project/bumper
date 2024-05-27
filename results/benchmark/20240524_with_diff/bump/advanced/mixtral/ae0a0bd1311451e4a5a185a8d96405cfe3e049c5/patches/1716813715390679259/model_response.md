Here is a possible patch for the failing client code:
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
The error message indicates that the constructor of `StringContains` now requires a single `String` argument, instead of a `boolean` and a `String`. To fix this, I have replaced the `false` argument with a string that contains the expected substring. I have also added a separate variable `contains` to store the result of the `contains` method, to make the code clearer.