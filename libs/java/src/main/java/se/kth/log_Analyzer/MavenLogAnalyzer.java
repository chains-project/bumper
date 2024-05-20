package se.kth.log_Analyzer;


import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MavenLogAnalyzer {

    private final File logFile;

    public MavenLogAnalyzer(File logFile) {
        this.logFile = logFile;
    }

    public MavenErrorLog analyzeCompilationErrors() throws IOException {
        return extractLineNumbersWithPaths(logFile.getAbsolutePath());
    }


    private MavenErrorLog extractLineNumbersWithPaths(String logFilePath) throws IOException {
        MavenErrorLog mavenErrorLogs = new MavenErrorLog();

        try {
            FileInputStream fileInputStream = new FileInputStream(logFilePath);
            InputStreamReader inputStreamReader = new InputStreamReader(fileInputStream, StandardCharsets.ISO_8859_1);
            BufferedReader reader = new BufferedReader(inputStreamReader);
            String line;
            String currentPath = null;
            Pattern errorPattern = Pattern.compile("\\[ERROR\\] .*:\\[(\\d+),\\d+\\]");
            Pattern pathPattern = Pattern.compile("/[^:/]+(/[^\\[\\]:]+)");

            while ((line = reader.readLine()) != null) {
                Matcher matcher = errorPattern.matcher(line);
                if (matcher.find()) {
                    Integer lineNumber = Integer.valueOf(matcher.group(1));
                    Matcher pathMatcher = pathPattern.matcher(line);

                    if (pathMatcher.find()) {
                        currentPath = pathMatcher.group();
                    }

                    if (currentPath != null) {
                        mavenErrorLogs.addErrorInfo(
                            currentPath, 
                            new MavenErrorLog.ErrorInfo(String.valueOf(lineNumber), currentPath, line)
                                .setAdditionalInfo(
                                    this.extractAdditionalInfo(reader)
                                )
                        );
                    }
                }

            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return mavenErrorLogs;
    }

    private String extractAdditionalInfo(BufferedReader fromReader) {
        String line = null;
        int charRead = -1;

        try {
            // Read first char of new line and reset the buffer
            fromReader.mark(1);
			charRead = fromReader.read();
            fromReader.reset();

            if(((char) charRead) == ' ') {
                line = fromReader.readLine();
                if(line == null) {
                    return "";
                } else {
                    return line + "\n" + extractAdditionalInfo(fromReader);
                }
            } else {
                return "";
			}
		} catch (IOException e) {
            e.printStackTrace();
            return "";
		}
    }
}