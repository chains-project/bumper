```java
import org.apache.maven.project.MavenProject;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.plugins.annotations.ResolutionScope;
import org.apache.maven.shared.filtering.MavenFilteringException;
import org.apache.maven.shared.filtering.MavenResourcesExecution;
import org.apache.maven.shared.filtering.MavenResourcesFiltering;
import org.apache.maven.shared.filtering.DefaultMavenResourcesFiltering;
import org.apache.maven.shared.utils.io.FileUtils;
import org.apache.maven.shared.utils.io.IOExceptionHandler;
import org.apache.maven.shared.utils.io.MessageUtils;
import org.apache.maven.shared.utils.io.logging.DefaultMessageBuilder;
import org.apache.maven.shared.utils.io.logging.DefaultMessageCapturer;
import org.apache.maven.shared.utils.io.logging.MessageBuilder;
import org.apache.maven.shared.utils.io.logging.MessageCapturer;
import org.apache.maven.shared.utils.io.logging.MessageHolder;
import org.apache.maven.shared.utils.io.logging.MessageUtils.MessageSeverity;
import org.apache.maven.shared.utils.io.logging.ThreadBoundMessageCapturer;
import org.apache.maven.shared.utils.io.logging.ThreadBoundMessageHolder;
import org.apache.maven.shared.utils.logging.MessageUtils2;
import org.codehaus.plexus.logging.Logger;
import org.codehaus.plexus.logging.console.ConsoleLogger;
import org.codehaus.plexus.util.StringUtils;
import org.codehaus.plexus.util.xml.pull.XmlPullParserException;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
```