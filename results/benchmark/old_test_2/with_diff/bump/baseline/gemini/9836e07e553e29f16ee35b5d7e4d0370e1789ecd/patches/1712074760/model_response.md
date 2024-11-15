```java
import static org.hamcrest.CoreMatchers.containsString;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertThrows;

import com.artipie.docker.Tag.Valid;
import com.artipie.docker.TagValidTest;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class TagValidTestFixed {

    @ParameterizedTest
    @ValueSource(strings = {
        "",
        ".0",
        "*",
        "\u00ea",
        "-my-tag",
        //@checkstyle LineLengthCheck (1 line)
        "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678"
    })
    void shouldFailToGetValueWhenInvalid(final String original) {
        final Valid tag = new Valid(original);
        assertThat(tag.valid(), containsString("false"));
        final Throwable throwable = assertThrows(
            InvalidTagNameException.class,
            tag::value
        );
        assertThat(
            throwable.getMessage(),
            containsString("Invalid tag")
        );
    }
}
```