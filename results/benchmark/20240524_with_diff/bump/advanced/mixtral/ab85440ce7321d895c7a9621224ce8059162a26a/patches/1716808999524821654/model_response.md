Here is a patch that you can apply to the code in order to fix the error:
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
The error message indicates that the constructor for `StringContains` is expecting a single `String` argument, but is instead receiving a `boolean` and a `String`. To fix this, I have replaced the usage of `StringContains` with a call to the `contains` method on the `output` string. I have also added a new variable `contains` to store the result of this method call.

Additionally, I have updated the `assertThat` statement to use the `StringContains` constructor that takes a single `String` argument, and have used string concatenation to construct the expected value.

I hope this helps! Let me know if you have any questions.