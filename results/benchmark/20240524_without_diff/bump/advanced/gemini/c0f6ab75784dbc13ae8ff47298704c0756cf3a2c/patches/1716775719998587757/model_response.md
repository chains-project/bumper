```java
import java.util.Set;
import org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration;
import org.sonarsource.sonarlint.core.analysis.api.AnalysisEngineConfiguration.Builder;
import org.sonarsource.sonarlint.core.commons.Language;

private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    Builder builder = AnalysisEngineConfiguration.builder();
    
    Set<Language> enabledLanguages = sorald.sonar.SonarLintEngine.globalConfig.getEnabledLanguages();
    if (enabledLanguages != null) {
        builder.addEnabledLanguages(enabledLanguages);
    }
    
    builder.setClientPid(sorald.sonar.SonarLintEngine.globalConfig.getClientPid());
    builder.setExtraProperties(sorald.sonar.SonarLintEngine.globalConfig.extraProperties());
    builder.setWorkDir(sorald.sonar.SonarLintEngine.globalConfig.getWorkDir());
    builder.setModulesProvider(sorald.sonar.SonarLintEngine.globalConfig.getModulesProvider());
    
    return builder.build();
}
```