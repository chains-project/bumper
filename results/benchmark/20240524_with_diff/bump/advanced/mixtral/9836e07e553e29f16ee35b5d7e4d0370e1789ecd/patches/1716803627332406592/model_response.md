Here is a suggested patch for the client code:
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
The failure is caused by the fact that the constructor for `StringContains` no longer accepts a second boolean argument. To fix this, I have replaced the call to `StringContains` with a new instance created using the `StringContains` constructor that accepts a single `String` argument. I have also added a separate variable to store the result of the `contains` method on the `output` string. This allows the `assertThat` statement to check if the `output` string contains the expected substring.