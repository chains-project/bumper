```java
@org.junit.jupiter.api.Test
void largeImageUploadWorks() throws java.lang.Exception {
    try {
        this.buildImage();
        final java.lang.String output = this.client.run("push", this.remote());
        org.hamcrest.MatcherAssert.assertThat(output, org.hamcrest.core.StringMatchers.containsString("Pushed"));
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```