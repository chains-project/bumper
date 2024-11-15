```java
import java.io.IOException;

import com.artipie.http.headers.Header;
import com.artipie.http.rs.RsStatus;
import com.artipie.http.rs.RsWithBody;
import com.artipie.http.rs.RsWithHeaders;
import com.artipie.http.rs.StandardRs;
import com.artipie.security.Policy;
import com.artipie.security.policy.YamlPolicyFactory;
import com.google.common.base.Strings;
import com.google.common.io.ByteStreams;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Optional;

/**
 * Represents a policy factory based on YAML representation.
 *
 * @since 0.1
 */
public final class YamlPolicyFactory implements Policy.Factory {

    /**
     * Base directory for policies.
     */
    private final String base;

    /**
     * Ctor.
     *
     * @param base Base directory for policies.
     */
    public YamlPolicyFactory(final String base) {
        this.base = base;
    }

    @Override
    public Optional<Policy> policy(final String name) {
        final String path = Strings.isNullOrEmpty(name) ? this.base : this.base + name;
        return Optional.ofNullable(path).flatMap(
            p -> {
                try (InputStream stream = YamlPolicyFactory.class.getResourceAsStream(p)) {
                    return Optional.ofNullable(stream)
                        .map(
                            is -> new YamlPolicyFactory.YamlPolicy(
                                ByteStreams.toByteArray(is),
                                new Header("Content-Type", "application/x-yaml")
                            )
                        );
                } catch (final IOException e) {
                    throw new UncheckedIOException(e);
                }
            }
        );
    }

    /**
     * YAML policy.
     *
     * @since 0.1
     */
    private static final class YamlPolicy implements Policy {

        /**
         * Policy content.
         */
        private final byte[] content;

        /**
         * Policy content type.
         */
        private final Header contentType;

        /**
         * Ctor.
         *
         * @param content Policy content.
         * @param contentType Policy content type.
         */
        YamlPolicy(final byte[] content, final Header contentType) {
            this.content = content;
            this.contentType = contentType;
        }

        @Override
        public RsWithBody.Proxy asRs() {
            return new RsWithHeaders.Proxy(
                new StandardRs(
                    RsStatus.OK,
                    this.contentType,
                    this.content
                )
            );
        }
    }
}
```