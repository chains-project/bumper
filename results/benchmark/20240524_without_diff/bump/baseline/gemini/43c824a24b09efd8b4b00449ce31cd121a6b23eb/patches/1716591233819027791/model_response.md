```java
import de.gwdg.metadataqa.api.json.JsonBranch;
import de.gwdg.metadataqa.api.json.JsonCommit;
import de.gwdg.metadataqa.api.json.JsonFile;
import de.gwdg.metadataqa.api.json.JsonRepository;
import de.gwdg.metadataqa.api.json.JsonUser;
import org.eclipse.jgit.api.Git;
import org.eclipse.jgit.api.errors.GitAPIException;
import org.eclipse.jgit.lib.Repository;
import org.eclipse.jgit.revwalk.RevCommit;
import org.eclipse.jgit.revwalk.RevWalk;
import org.eclipse.jgit.transport.CredentialsProvider;
import org.eclipse.jgit.transport.UsernamePasswordCredentialsProvider;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class MarcFactory {

    private static final String GIT_URL = "https://github.com/gwdg/metadata-qa-catalogue.git";
    private static final String BRANCH_NAME = "master";
    private static final String USERNAME = "username";
    private static final String PASSWORD = "password";

    public static List<JsonBranch> getBranches(String repositoryUrl, String branchName, String username, String password) throws IOException, GitAPIException {
        List<JsonBranch> branches = new ArrayList<>();
        CredentialsProvider credentialsProvider = new UsernamePasswordCredentialsProvider(username, password);
        try (Git git = Git.open(new File(repositoryUrl))) {
            git.pull().setCredentialsProvider(credentialsProvider).call();
            try (RevWalk walk = new RevWalk(git.getRepository())) {
                RevCommit commit = walk.parseCommit(git.getRepository().resolve(branchName + "^{commit}"));
                for (RevCommit parent : commit.getParents()) {
                    JsonBranch branch = new JsonBranch();
                    branch.setName(parent.getName());
                    branch.setCommit(new JsonCommit(parent.getName(), parent.getAuthorIdent().getName(), parent.getAuthorIdent().getEmailAddress(), parent.getFullMessage()));
                    branches.add(branch);
                }
            }
        }
        return branches;
    }

    public static List<JsonFile> getFiles(String repositoryUrl, String branchName, String username, String password) throws IOException, GitAPIException {
        List<JsonFile> files = new ArrayList<>();
        CredentialsProvider credentialsProvider = new UsernamePasswordCredentialsProvider(username, password);
        try (Git git = Git.open(new File(repositoryUrl))) {
            git.pull().setCredentialsProvider(credentialsProvider).call();
            Repository repository = git.getRepository();
            for (RevCommit commit : git.log().call()) {
                for (RevCommit parent : commit.getParents()) {
                    for (String fileName : parent.getModifiedFilePaths()) {
                        JsonFile file = new JsonFile();
                        file.setName(fileName);
                        file.setCommit(new JsonCommit(parent.getName(), parent.getAuthorIdent().getName(), parent.getAuthorIdent().getEmailAddress(), parent.getFullMessage()));
                        files.add(file);
                    }
                }
            }
        }
        return files;
    }

    public static List<JsonCommit> getCommits(String repositoryUrl, String branchName, String username, String password) throws IOException, GitAPIException {
        List<JsonCommit> commits = new ArrayList<>();
        CredentialsProvider credentialsProvider = new UsernamePasswordCredentialsProvider(username, password);
        try (Git git = Git.open(new File(repositoryUrl))) {
            git.pull().setCredentialsProvider(credentialsProvider).call();
            Repository repository = git.getRepository();
            for (RevCommit commit : git.log().call()) {
                JsonCommit jsonCommit = new JsonCommit();
                jsonCommit.setName(commit.getName());
                jsonCommit.setAuthor(commit.getAuthorIdent().getName());
                jsonCommit.setEmail(commit.getAuthorIdent().getEmailAddress());
                jsonCommit.setMessage(commit.getFullMessage());
                commits.add(jsonCommit);
            }
        }
        return commits;
    }

    public static JsonRepository getRepository(String repositoryUrl, String branchName, String username, String password) throws IOException, GitAPIException {
        JsonRepository repository = new JsonRepository();
        repository.setUrl(repositoryUrl);
        repository.setBranches(getBranches(repositoryUrl, branchName, username, password));
        repository.setFiles(getFiles(repositoryUrl, branchName, username, password));
        repository.setCommits(getCommits(repositoryUrl, branchName, username, password));
        return repository;
    }

    public static JsonUser getUser(String username, String password) {
        JsonUser user = new JsonUser();
        user.setUsername(username);
        user.setPassword(password);
        return user;
    }

    public static void main(String[] args) throws IOException, GitAPIException {
        JsonRepository repository = getRepository(GIT_URL, BRANCH_NAME, USERNAME, PASSWORD);
        System.out.println(repository);
    }
}
```