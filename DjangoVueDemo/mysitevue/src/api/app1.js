export function touchDemoAPI(id) {
    return request({
        url: '/touch/' + id + '/',
        method: 'get',
    })
}