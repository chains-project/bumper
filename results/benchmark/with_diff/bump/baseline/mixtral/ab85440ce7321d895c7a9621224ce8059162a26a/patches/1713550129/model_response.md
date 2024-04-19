Here is a possible patch for the failing code:
```java
@Test
void shouldPullPushedByTag() throws Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final String output = this.client.run("pull", this.image.remote());
    MatcherAssert.assertThat(
        output,
        new StringStartsWith(
            String.format("Status: Downloaded newer image for %s", this.image.remote())
        )
    );
}
```
The only change I made is to replace the `StringContains` matcher with the `StringStartsWith` matcher, which takes a single argument. This should fix the error message you were seeing, which was caused by the fact that the `StringContains` constructor now requires a single argument, whereas it used to accept two arguments.

Note that I did not use any of the removed library methods (indicated with `--`), and I did not use any of the added library methods (indicated with `++`). I only used the `StringStartsWith` matcher, which is part of the Hamcrest library and was not affected by the update.

I hope this helps! Let me know if you have any questions or if you need further assistance.