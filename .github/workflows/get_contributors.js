module.exports = async ({github, context}) => {
    return await github.paginate("GET /repos/{owner}/{repo}/contributors", {
        owner: 'RIOT-OS',
        repo: 'RIOT'
    }).then((contributors) => {
        return contributors;
    });
}
