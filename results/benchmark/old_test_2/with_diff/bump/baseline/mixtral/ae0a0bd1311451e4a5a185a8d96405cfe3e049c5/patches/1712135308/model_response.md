Here's a possible patch for the failing code:

```java
@Test
void shouldPullPushedByTag() throws Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    String output = this.client.run("pull", this.image.remote());
    MatcherAssert.assertThat(
        output,
        new StringContains("Status: Downloaded newer image for " + this.image.remote())
    );
}
```

The change I made is to remove the `false` argument from the `StringContains` constructor. The updated method call now only includes a single argument, which matches the expected constructor signature.